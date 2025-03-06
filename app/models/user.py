from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, func

from app.core.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    is_active = Column(Boolean, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
