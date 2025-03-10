import datetime
from pydantic import BaseModel, ConfigDict
from bson import ObjectId

from app.models.enums import NotificationStatusEnum, NotificationPriorityEnum



class Notification(BaseModel):
    id: str | None = None
    user_id: str # reference to user in postgres
    message: str
    status: NotificationStatusEnum = NotificationStatusEnum.unread
    priority: NotificationPriorityEnum = NotificationPriorityEnum.normal
    created_at: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)

    model_config = ConfigDict(
        from_attributes=True, 
        json_encoders={ObjectId: str}
    )