# app/database/db_connection.py
import sqlite3

DB_NAME = "task_system.db"

def create_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def init_db():
    conn = create_connection()
    cursor = conn.cursor()
    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    # Tasks table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT,
            description TEXT,
            priority TEXT,
            status TEXT DEFAULT 'Pending',
            deadline TEXT,
            created_date TEXT
        )
    """)
    conn.commit()
    conn.close()