from fastapi import APIRouter, Header, HTTPException
import jwt
from app.services.task_service import TaskService
from app.services.auth_service import SECRET_KEY

router = APIRouter()

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["user_id"]
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/tasks")
def create_task(title: str, description: str = "", deadline: str = "", priority: str = "Low", authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    user_id = verify_token(token)
    return TaskService.add_task(user_id, title, description, deadline, priority)

@router.get("/tasks")
def get_tasks(authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    user_id = verify_token(token)
    return TaskService.get_tasks(user_id)