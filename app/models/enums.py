from enum import Enum

from pydantic import BaseModel, ValidationError


class NotificationStatusEnum(Enum):
    unread = "unread"
    read = "read"
    deleted = "deleted"


class NotificationPriorityEnum(Enum):
    low = "low"
    normal = "normal"
    high = "high"