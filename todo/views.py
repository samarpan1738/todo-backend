from rest_framework.views import APIView
from rest_framework.response import Response
import todo_project.utils.health as health_util
from .constants.health import HealthStatus, ComponentHealthStatus


class HealthView(APIView):
    def get(self, request, format=None):
        is_db_healthy = health_util.is_db_healthy()
        db_status = ComponentHealthStatus.UP.name if is_db_healthy else ComponentHealthStatus.DOWN.name
        overall_status = HealthStatus.UP.name if is_db_healthy else HealthStatus.PARTIAL_FAILURE.name
        response = {
            "status": overall_status,
            "components": {
                "db": {"status": db_status},
            },
        }
        return Response(response)
