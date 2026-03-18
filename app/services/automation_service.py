# app/services/automation_service.py
from datetime import datetime
from app.database.db_connection import create_connection

class AutomationService:

    @staticmethod
    def overdue_tasks(user_id):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT title, deadline 
            FROM tasks 
            WHERE user_id=? AND status!='Completed' AND deadline<? 
        """, (user_id, now))
        overdue = cursor.fetchall()
        conn.close()
        return overdue