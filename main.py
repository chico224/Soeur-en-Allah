from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import engine, get_db
from datetime import datetime

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Soeur en Allah API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Journal endpoints
@app.post("/api/journal/", response_model=schemas.JournalEntry)
def create_journal_entry(entry: schemas.JournalEntryCreate, db: Session = Depends(get_db)):
    db_entry = models.JournalEntry(
        title=entry.title,
        content=entry.content,
        date=datetime.now(),
        user_id=1  # TODO: Implement proper user authentication
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

@app.get("/api/journal/", response_model=List[schemas.JournalEntry])
def get_journal_entries(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    entries = db.query(models.JournalEntry).offset(skip).limit(limit).all()
    return entries

# Confession endpoints
@app.post("/api/confession/", response_model=schemas.Confession)
def create_confession(confession: schemas.ConfessionCreate, db: Session = Depends(get_db)):
    db_confession = models.Confession(
        title=confession.title,
        content=confession.content,
        anonymous=confession.anonymous,
        date=datetime.now()
    )
    db.add(db_confession)
    db.commit()
    db.refresh(db_confession)
    return db_confession

# Quran endpoints
@app.get("/api/quran/surahs/")
def get_surahs(db: Session = Depends(get_db)):
    surahs = db.query(models.Surah).all()
    return surahs

@app.get("/api/quran/surah/{surah_id}")
def get_surah(surah_id: int, db: Session = Depends(get_db)):
    surah = db.query(models.Surah).filter(models.Surah.id == surah_id).first()
    if not surah:
        raise HTTPException(status_code=404, detail="Surah not found")
    return surah

# Goals endpoints
@app.post("/api/goals/", response_model=schemas.Goal)
def create_goal(goal: schemas.GoalCreate, db: Session = Depends(get_db)):
    db_goal = models.Goal(
        title=goal.title,
        description=goal.description,
        target_date=goal.target_date,
        user_id=1  # TODO: Implement proper user authentication
    )
    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)
    return db_goal

@app.get("/api/goals/", response_model=List[schemas.Goal])
def get_goals(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    goals = db.query(models.Goal).offset(skip).limit(limit).all()
    return goals
