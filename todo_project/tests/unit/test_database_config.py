from unittest import TestCase
from unittest.mock import patch, MagicMock
from todo_project.db.config import get_database_client, get_database
from pymongo import MongoClient
from pymongo.database import Database

TEST_DATABASE_URI = "mongodb://localhost:27017"
TEST_DATABASE_NAME = "todo-app"


class DatabaseConfigTests(TestCase):
    def setUp(self):
        self.db_client_patcher = patch("todo_project.db.config.database_client", None)
        self.db_patcher = patch("todo_project.db.config.db", None)
        self.db_client_patcher.start()
        self.db_patcher.start()

    def tearDown(self):
        self.db_client_patcher.stop()
        self.db_patcher.stop()

    @patch("todo_project.db.config.MongoClient")
    @patch("django.conf.settings")
    def test_get_db_client_initializes_client_when_called_first_time(self, mock_settings, mock_mongo_client):
        mock_settings.MONGODB_URI = TEST_DATABASE_URI
        mock_client_instance = MagicMock(spec=MongoClient)
        mock_mongo_client.return_value = mock_client_instance

        db_client = get_database_client()

        mock_mongo_client.assert_called_once_with(TEST_DATABASE_URI)

        self.assertEqual(db_client, mock_client_instance)

    @patch("todo_project.db.config.MongoClient")
    @patch("django.conf.settings")
    def test_get_db_client_reuses_existing_client_when_called_after_initialization(
        self, mock_settings, mock_mongo_client
    ):
        mock_settings.MONGODB_URI = TEST_DATABASE_URI
        mock_client_instance = MagicMock(spec=MongoClient)
        mock_mongo_client.return_value = mock_client_instance

        db_client1 = get_database_client()
        db_client2 = get_database_client()

        mock_mongo_client.assert_called_once()
        self.assertEqual(db_client1, db_client2)

    @patch("todo_project.db.config.get_database_client")
    @patch("django.conf.settings")
    def test_get_database_fetches_db_when_called_first_time(self, mock_settings, mock_get_database_client):
        mock_settings.DB_NAME = TEST_DATABASE_NAME
        mock_client = MagicMock(spec=MongoClient)
        mock_database_instance = MagicMock(spec=Database)
        mock_client.__getitem__.return_value = mock_database_instance
        mock_get_database_client.return_value = mock_client

        db_instance = get_database()

        mock_get_database_client.assert_called_once()

        mock_client.__getitem__.assert_called_once_with(TEST_DATABASE_NAME)

        self.assertEqual(db_instance, mock_database_instance)

    @patch("todo_project.db.config.get_database_client")
    @patch("django.conf.settings")
    def test_get_database_reuses_existing_db_when_called_after_initialization(
        self, mock_settings, mock_get_database_client
    ):
        mock_settings.DB_NAME = TEST_DATABASE_NAME
        mock_client = MagicMock(spec=MongoClient)
        mock_database_instance = MagicMock(spec=Database)
        mock_client.__getitem__.return_value = mock_database_instance
        mock_get_database_client.return_value = mock_client

        db_instance1 = get_database()
        db_instance2 = get_database()

        mock_get_database_client.assert_called_once()

        self.assertEqual(db_instance1, db_instance2)
