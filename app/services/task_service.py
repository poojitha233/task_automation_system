# app/services/task_service.py
from datetime import datetime
from app.database.db_connection import create_connection

class TaskService:
    @staticmethod
    def add_task(user_id: int, task):
        conn = create_connection()
        cursor = conn.cursor()
        created = datetime.today().strftime("%Y-%m-%d")
        cursor.execute(
            "INSERT INTO tasks (user_id, title, description, priority, status, deadline, created_date) VALUES (?, ?, ?, ?, 'Pending', ?, ?)",
            (user_id, task.title, task.description, task.priority, str(task.deadline), created)
        )
        conn.commit()
        task_id = cursor.lastrowid
        conn.close()
        return {"message": "Task added successfully", "id": task_id}

    @staticmethod
    def get_tasks(user_id: int):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE user_id=?", (user_id,))
        rows = cursor.fetchall()
        conn.close()
        tasks = []
        for r in rows:
            tasks.append({
                "id": r[0],
                "title": r[2],
                "description": r[3],
                "priority": r[4],
                "status": r[5],
                "deadline": r[6],
                "created_date": r[7]
            })
        return tasks

    @staticmethod
    def update_task(user_id: int, task_id: int, task):
        conn = create_connection()
        cursor = conn.cursor()
        existing = cursor.execute("SELECT * FROM tasks WHERE id=? AND user_id=?", (task_id, user_id)).fetchone()
        if not existing:
            conn.close()
            return {"message": "Task not found"}
        # Update only provided fields
        cursor.execute("""
            UPDATE tasks SET title=COALESCE(?, title),
                             description=COALESCE(?, description),
                             priority=COALESCE(?, priority),
                             status=COALESCE(?, status),
                             deadline=COALESCE(?, deadline)
            WHERE id=? AND user_id=?
        """, (task.title, task.description, task.priority, task.status, str(task.deadline) if task.deadline else None, task_id, user_id))
        conn.commit()
        conn.close()
        return {"message": "Task updated successfully"}

    @staticmethod
    def delete_task(user_id: int, task_id: int):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id=? AND user_id=?", (task_id, user_id))
        conn.commit()
        conn.close()
        return {"message": "Task deleted successfully"}