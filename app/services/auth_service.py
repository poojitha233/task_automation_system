# app/services/auth_service.py
import hashlib
import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException
from app.database.db_connection import create_connection

SECRET_KEY = "secret123"

class AuthService:
    @staticmethod
    def register(username: str, password: str):
        conn = create_connection()
        cursor = conn.cursor()
        hashed = hashlib.sha256(password.encode()).hexdigest()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
            conn.commit()
            user_id = cursor.lastrowid
            return {"message": "User registered successfully", "user_id": user_id}
        except:
            return {"message": "Username already exists"}
        finally:
            conn.close()

    @staticmethod
    def login(username: str, password: str):
        conn = create_connection()
        cursor = conn.cursor()
        hashed = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("SELECT id FROM users WHERE username=? AND password=?", (username, hashed))
        row = cursor.fetchone()
        conn.close()
        if row:
            token_data = {"user_id": row[0], "exp": datetime.utcnow() + timedelta(hours=12)}
            token = jwt.encode(token_data, SECRET_KEY, algorithm="HS256")
            return token
        return None

    @staticmethod
    def verify_token(token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return payload["user_id"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except:
            raise HTTPException(status_code=401, detail="Invalid token")