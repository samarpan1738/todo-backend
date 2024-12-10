from todo.constants.task import TaskPriority
from todo.models.task import TaskModel
from todo.constants.task import TaskStatus
from bson import ObjectId

tasks_models = [
    TaskModel(
        id=ObjectId(),
        displayId="#1",
        title="Task 1",
        description="Test task 1",
        priority=TaskPriority.HIGH,
        status=TaskStatus.TODO,
        assignee="qMbT6M2GB65W7UHgJS4g",
        isAcknowledged=True,
        labels=[ObjectId(), ObjectId()],
        createdAt="2024-11-08T10:14:35",
        updatedAt="2024-11-08T15:14:35",
        createdBy="qMbT6M2GB65W7UHgJS4g",
        updatedBy="qMbT6M2GB65W7UHgJS4g",
    ),
    TaskModel(
        id=ObjectId(),
        displayId="#2",
        title="Task 2",
        description="Test task 2",
        priority=TaskPriority.MEDIUM,
        status=TaskStatus.IN_PROGRESS,
        assignee="qMbT6M2GB65W7UHgJS4g",
        isAcknowledged=True,
        labels=[ObjectId(), ObjectId()],
        startedAt="2024-11-09T09:14:35",
        createdAt="2024-11-08T10:14:35",
        updatedAt="2024-11-08T15:14:35",
        createdBy="qMbT6M2GB65W7UHgJS4g",
        updatedBy="qMbT6M2GB65W7UHgJS4g",
    ),
]
