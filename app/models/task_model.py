# app/models/task_model.py
from pydantic import BaseModel
from typing import Optional
from datetime import date

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str
    deadline: date

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None  # Pending/Completed
    deadline: Optional[date] = None