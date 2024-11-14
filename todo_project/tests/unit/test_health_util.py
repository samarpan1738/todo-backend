from unittest import TestCase
from unittest.mock import patch, MagicMock
from pymongo.errors import ConnectionFailure
from todo_project.utils.health import is_db_healthy


class DatabaseConfigTests(TestCase):
    def setUp(self):
        self.db_client_patcher = patch("todo_project.db.config.database_client", None)
        self.db_client_patcher.start()

    def tearDown(self):
        self.db_client_patcher.stop()

    @patch("todo_project.utils.health.get_database_client")
    def test_db_health_check_when_connection_successful(self, mock_get_database_client):
        # Mocking the success scenario
        mock_client = MagicMock()
        mock_client.admin.command.return_value = {"ok": 1}
        mock_get_database_client.return_value = mock_client

        # Call the function under test
        result = is_db_healthy()

        # Assertions for success scenario
        self.assertTrue(result)
        mock_get_database_client.assert_called_once()
        mock_client.admin.command.assert_called_once_with("ping")

    @patch("todo_project.utils.health.get_database_client")
    def test_db_health_check_when_connection_failure(self, mock_get_database_client):
        mock_client = MagicMock()
        mock_client.admin.command.side_effect = ConnectionFailure("Mocked connection failure")
        mock_get_database_client.return_value = mock_client

        result = is_db_healthy()

        self.assertFalse(result)
        mock_get_database_client.assert_called_once()
        mock_client.admin.command.assert_called_once_with("ping")
