​🚀 Intelligent Task Automation & Productivity Management System
​A Python-based backend system designed to automate task management and improve personal productivity through secure APIs and data analytics.  
​🛠 Tech Stack
​Backend Framework: FastAPI.  
​Database: SQLite (using Task_system.db).  
​Authentication: JWT (JSON Web Tokens) and OAuth2PasswordBearer.  
​Server: Uvicorn ASGI server.  
​
✨ Key Features
​User Authentication: Secure registration and login workflows.  
​Task CRUD Operations: Full capability to Create, Read, Update, and Delete tasks.  
​Productivity Analytics: A dedicated service providing summaries of task status and progress.  
​Data Portability: Integrated feature to export task lists into CSV format.  
​Interactive API Docs: Built-in Swagger UI for real-time API testing at /docs.  

​📁 Project Structure
​app/models/: Pydantic schemas for data validation, including UserCreate and UserOut.  
​app/services/: Core business logic, such as TaskService and AuthService.  
​app/database/: Connection management and database initialization via db_connection.py.  

​🚀 Installation & Setup
​For Mac Users
1.Open Terminaland navigate to the project directory. 
2.Create a virtual environment:
python3 -m venv venv

3.Activate the Environment:
source venv/bin/activate

4.Install Dependencies:
pip install -r requirements.txt

5.Run the Application:
uvicorn main:app --reload

->For the windows users
1.​Open Command Prompt or PowerShell in the project directory.
2.Create a virtual environment:
python -m venv venv

3.Activate the Environment:
.\venv\Scripts\activate

4.Install Dependencies:
pip install -r requirements.txt

5.​Run the Application:
uvicorn main:app --reload
💡 Accessing the System
​Once the server is running, you can access the interactive documentation to test the APIs at:
http://127.0.0.1:8000/docs. 





