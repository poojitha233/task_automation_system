# main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.database.db_connection import init_db
from app.services.auth_service import AuthService
from app.services.task_service import TaskService
from app.services.analytics_service import AnalyticsService
from app.services.file_service import FileService
from app.models.task_model import TaskCreate, TaskUpdate

app = FastAPI(title="Intelligent Task Automation API")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

init_db()

# ---------------- AUTH ----------------
@app.post("/register")
def register(username: str, password: str):
    return AuthService.register(username, password)

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    token = AuthService.login(form_data.username, form_data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}

# ---------------- TASKS ----------------
@app.post("/tasks")
def add_task(task: TaskCreate, token: str = Depends(oauth2_scheme)):
    user_id = AuthService.verify_token(token)
    return TaskService.add_task(user_id, task)

@app.get("/tasks")
def get_tasks(token: str = Depends(oauth2_scheme)):
    user_id = AuthService.verify_token(token)
    return TaskService.get_tasks(user_id)

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate, token: str = Depends(oauth2_scheme)):
    user_id = AuthService.verify_token(token)
    return TaskService.update_task(user_id, task_id, task)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, token: str = Depends(oauth2_scheme)):
    user_id = AuthService.verify_token(token)
    return TaskService.delete_task(user_id, task_id)

# ---------------- ANALYTICS ----------------
@app.get("/analytics")
def analytics(token: str = Depends(oauth2_scheme)):
    user_id = AuthService.verify_token(token)
    return AnalyticsService.get_summary(user_id)

# ---------------- FILE ----------------
@app.get("/tasks/export")
def export_csv(token: str = Depends(oauth2_scheme)):
    user_id = AuthService.verify_token(token)
    return FileService.export_tasks_csv(user_id)

@app.get("/tasks/backup")
def backup_json(token: str = Depends(oauth2_scheme)):
    user_id = AuthService.verify_token(token)
    return FileService.backup_tasks_json(user_id)