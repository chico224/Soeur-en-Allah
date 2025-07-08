from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    journal_entries = relationship("JournalEntry", back_populates="user")
    goals = relationship("Goal", back_populates="user")

class JournalEntry(Base):
    __tablename__ = "journal_entries"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="journal_entries")

class Confession(Base):
    __tablename__ = "confessions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)
    anonymous = Column(Boolean, default=True)
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    user = relationship("User", back_populates="confessions")

class Surah(Base):
    __tablename__ = "surahs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    ayah_count = Column(Integer)
    english_name = Column(String)
    order = Column(Integer)

class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    target_date = Column(DateTime)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="goals")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    description = Column(Text)
    cover_image = Column(String)
    file_path = Column(String)
    category = Column(String)

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    date = Column(DateTime)
    type = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
