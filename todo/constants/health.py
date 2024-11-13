from enum import Enum


class HealthStatus(Enum):
    UP = 1
    PARTIAL_FAILURE = 2


class ComponentHealthStatus(Enum):
    UP = 1
    DOWN = 2
