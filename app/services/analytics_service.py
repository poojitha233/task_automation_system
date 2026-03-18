# app/services/analytics_service.py
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from app.database.db_connection import create_connection

class AnalyticsService:

    @staticmethod
    def show_summary(user_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT status FROM tasks WHERE user_id=?", (user_id,))
        tasks = cursor.fetchall()
        conn.close()

        if not tasks:
            print("No tasks to analyze.")
            return

        completed = sum(1 for t in tasks if t[0] == "Completed")
        pending = sum(1 for t in tasks if t[0] != "Completed")
        total = len(tasks)
        completion_percent = round((completed / total) * 100, 2)

        print(f"\n📊 Productivity Summary:")
        print(f"Total Tasks: {total}")
        print(f"Completed: {completed}")
        print(f"Pending: {pending}")
        print(f"Completion %: {completion_percent}%")

        # Simple pie chart
        plt.figure(figsize=(6,6))
        plt.pie([completed, pending], labels=["Completed", "Pending"], autopct="%1.1f%%", colors=["green", "orange"])
        plt.title("Task Completion Ratio")
        plt.show()