from pydantic import BaseModel, Field
from typing import ClassVar, List
from datetime import datetime

from todo.constants.task import TaskPriority, TaskStatus
from todo.models.common.document import Document

from todo.models.common.pyobjectid import PyObjectId
from todo_project.db.config import DatabaseManager

database_manager = DatabaseManager()


class DeferredDetailsModel(BaseModel):
    deferredAt: datetime | None = None
    deferredTill: datetime | None = None
    deferredBy: str | None = None

    class Config:
        from_attributes = True


class TaskModel(Document):
    collection_name: ClassVar[str] = "tasks"

    id: PyObjectId | None = Field(None, alias="_id")
    displayId: str
    title: str
    description: str | None = None
    priority: TaskPriority | None = None
    status: TaskStatus | None = None
    assignee: str | None = None
    isAcknowledged: bool | None = None
    labels: List[PyObjectId] | None = []
    isDeleted: bool = False
    deferredDetails: DeferredDetailsModel | None = None
    startedAt: datetime | None = None
    dueAt: datetime | None = None
    createdAt: datetime
    updatedAt: datetime | None = None
    createdBy: str
    updatedBy: str | None = None
