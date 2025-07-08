from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

class JournalEntryBase(BaseModel):
    title: str
    content: str

class JournalEntryCreate(JournalEntryBase):
    pass

class JournalEntry(JournalEntryBase):
    id: int
    date: datetime
    user_id: int

    class Config:
        from_attributes = True

class ConfessionBase(BaseModel):
    title: str
    content: str
    anonymous: bool = True

class ConfessionCreate(ConfessionBase):
    pass

class Confession(ConfessionBase):
    id: int
    date: datetime
    user_id: Optional[int] = None

    class Config:
        from_attributes = True

class Surah(BaseModel):
    id: int
    name: str
    ayah_count: int
    english_name: str
    order: int

    class Config:
        from_attributes = True

class GoalBase(BaseModel):
    title: str
    description: str
    target_date: datetime

class GoalCreate(GoalBase):
    pass

class Goal(GoalBase):
    id: int
    completed: bool
    user_id: int

    class Config:
        from_attributes = True

class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    cover_image: str
    file_path: str
    category: str

    class Config:
        from_attributes = True

class Event(BaseModel):
    id: int
    title: str
    description: str
    date: datetime
    type: str
    user_id: int

    class Config:
        from_attributes = True
