from fastapi import APIRouter
from fastapi import Query
from app.services.auth_service import AuthService

router = APIRouter()

@router.post("/register")
def register(username: str = Query(...), password: str = Query(...)):
    return AuthService.register(username, password)

@router.post("/login")
def login(username: str = Query(...), password: str = Query(...)):
    return AuthService.login(username, password)