from unittest import TestCase
from unittest.mock import patch, MagicMock

from django.conf import settings
from todo_project.db.config import DatabaseManager
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import ConnectionFailure


class DatabaseManagerTests(TestCase):
    def setUp(self):
        DatabaseManager._DatabaseManager__instance = None
        self.database_manager = DatabaseManager()

    def tearDown(self):
        self.database_manager = None

    @patch("todo_project.db.config.MongoClient")
    @patch("django.conf.settings")
    def test_initializes_db_client_on_first_call(self, mock_settings, mock_mongo_client):
        mock_settings.MONGODB_URI = settings.MONGODB_URI
        mock_client_instance = MagicMock(spec=MongoClient)
        mock_mongo_client.return_value = mock_client_instance
        db_client = self.database_manager._DatabaseManager__get_database_client()

        mock_mongo_client.assert_called_once_with(settings.MONGODB_URI)

        self.assertEqual(db_client, mock_client_instance)

    @patch("todo_project.db.config.MongoClient")
    @patch("django.conf.settings")
    def test_reuses_existing_db_client_on_subsequent_calls(self, mock_settings, mock_mongo_client):
        mock_settings.MONGODB_URI = settings.MONGODB_URI
        mock_client_instance = MagicMock(spec=MongoClient)
        mock_mongo_client.return_value = mock_client_instance

        db_client1 = self.database_manager._DatabaseManager__get_database_client()
        db_client2 = self.database_manager._DatabaseManager__get_database_client()

        mock_mongo_client.assert_called_once()
        self.assertEqual(db_client1, db_client2)

    @patch("todo_project.db.config.DatabaseManager._DatabaseManager__get_database_client")
    @patch("django.conf.settings")
    def test_initializes_db_on_first_call(self, mock_settings, mock_get_database_client):
        mock_settings.DB_NAME = settings.DB_NAME
        mock_client = MagicMock(spec=MongoClient)
        mock_database_instance = MagicMock(spec=Database)
        mock_client.__getitem__.return_value = mock_database_instance
        mock_get_database_client.return_value = mock_client

        db_instance = self.database_manager.get_database()

        mock_get_database_client.assert_called_once()

        mock_client.__getitem__.assert_called_once_with(settings.DB_NAME)

        self.assertEqual(db_instance, mock_database_instance)

    @patch("todo_project.db.config.DatabaseManager._DatabaseManager__get_database_client")
    @patch("django.conf.settings")
    def test_reuses_existing_db_on_subsequent_calls(self, mock_settings, mock_get_database_client):
        mock_settings.DB_NAME = settings.DB_NAME
        mock_client = MagicMock(spec=MongoClient)
        mock_database_instance = MagicMock(spec=Database)
        mock_client.__getitem__.return_value = mock_database_instance
        mock_get_database_client.return_value = mock_client

        db_instance1 = self.database_manager.get_database()
        db_instance2 = self.database_manager.get_database()

        mock_get_database_client.assert_called_once()

        self.assertEqual(db_instance1, db_instance2)

    @patch("todo_project.db.config.DatabaseManager._DatabaseManager__get_database_client")
    def test_check_db_health_returns_true_on_successful_connection(self, mock_get_database_client):
        # Mocking the success scenario
        mock_client = MagicMock()
        mock_client.admin.command.return_value = {"ok": 1}
        mock_get_database_client.return_value = mock_client

        # Call the function under test
        result = self.database_manager.check_db_health()

        # Assertions for success scenario
        self.assertTrue(result)
        mock_get_database_client.assert_called_once()
        mock_client.admin.command.assert_called_once_with("ping")

    @patch("todo_project.db.config.DatabaseManager._DatabaseManager__get_database_client")
    def test_check_db_health_returns_false_on_connection_failure(self, mock_get_database_client):
        mock_client = MagicMock()
        mock_client.admin.command.side_effect = ConnectionFailure("Mocked connection failure")
        mock_get_database_client.return_value = mock_client

        result = self.database_manager.check_db_health()

        self.assertFalse(result)
        mock_get_database_client.assert_called_once()
        mock_client.admin.command.assert_called_once_with("ping")
