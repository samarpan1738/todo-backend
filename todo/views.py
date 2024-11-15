from rest_framework.views import APIView
from rest_framework.response import Response
import todo_project.utils.health as health_util
from .constants.health import AppHealthStatus, ComponentHealthStatus


class HealthView(APIView):
    def get(self, request, format=None):
        is_db_healthy = health_util.is_db_healthy()
        db_status = ComponentHealthStatus.UP.name if is_db_healthy else ComponentHealthStatus.DOWN.name
        overall_status = AppHealthStatus.UP if is_db_healthy else AppHealthStatus.DOWN
        response = {
            "status": overall_status.name,
            "components": {
                "db": {"status": db_status},
            },
        }
        return Response(response, overall_status.http_status)
