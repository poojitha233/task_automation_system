# app/services/file_service.py
import csv
import json
from app.database.db_connection import create_connection

class FileService:

    @staticmethod
    def export_tasks_csv(user_id, filename="tasks.csv"):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE user_id=?", (user_id,))
        rows = cursor.fetchall()
        headers = [desc[0] for desc in cursor.description]
        conn.close()

        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)
        print(f"✅ Tasks exported to {filename}")

    @staticmethod
    def backup_tasks_json(user_id, filename="tasks_backup.json"):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE user_id=?", (user_id,))
        rows = cursor.fetchall()
        headers = [desc[0] for desc in cursor.description]
        conn.close()

        data = [dict(zip(headers, row)) for row in rows]

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"✅ Tasks backed up to {filename}")