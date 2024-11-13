from rest_framework.reverse import reverse
from rest_framework.test import APISimpleTestCase, APIClient
from rest_framework import status


class HealthAPITests(APISimpleTestCase):
    def setUp(self):
        self.client = APIClient()

    def test_health_check_api_success_case(self):
        url = reverse("health")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"status": "UP"})
