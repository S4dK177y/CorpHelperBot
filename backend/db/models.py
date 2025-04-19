from sqlmodel import SQLModel, Field
from datetime import datetime

class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    telegram_id: int
    full_name: str
    is_admin: bool = False

class VacationRequest(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int
    start_date: datetime
    end_date: datetime
    status: str = "pending"
    created_at: datetime = Field(default_factory=datetime.utcnow)