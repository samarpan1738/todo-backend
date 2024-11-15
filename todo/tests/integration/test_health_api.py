from rest_framework.reverse import reverse
from rest_framework.test import APISimpleTestCase, APIClient
from rest_framework import status
from unittest.mock import patch
from todo.constants.health import HealthStatus, ComponentHealthStatus


class HealthAPITests(APISimpleTestCase):
    def setUp(self):
        self.client = APIClient()

    @patch(target="todo_project.utils.health.is_db_healthy", return_value=True)
    def test_health_api_with_db_up_returns_success(self, mocked):
        url = reverse("health")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], HealthStatus.UP.name)
        self.assertEqual(response.data["components"]["db"]["status"], ComponentHealthStatus.UP.name)

    @patch(target="todo_project.utils.health.is_db_healthy", return_value=False)
    def test_health_api_with_db_down_returns_degraded_test(self, mocked):
        url = reverse("health")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)
        self.assertEqual(response.data["status"], HealthStatus.DEGRADED.name)
        self.assertEqual(response.data["components"]["db"]["status"], ComponentHealthStatus.DOWN.name)
