To-Do List Application: A robust web application built with Python and FastAPI for managing a To-Do list. This project implements a full RESTful API for CRUD operations, utilizes Jinja2 templates for a server-side rendered frontend, and uses SQLAlchemy for database management.

📋 Features

i) Task Management: Create, Read, and Update tasks.

ii) Web Interface: User-friendly HTML interface styled with Bootstrap.

iii) RESTful API: JSON-based API endpoints for external integration.

iv)Database: SQLite storage for persistent data management.

v) Auto-Documentation: Interactive API docs via Swagger UI.

🛠️ Tech Stack

i) Framework: FastAPI

ii) Language: Python 3.x

iii) Database: SQLite (via SQLAlchemy ORM)

iv) Templates: Jinja2

v) Testing: Pytest

vi) Server: Uvicorn

🚀 Installation & Setup: Follow these steps to set up the project locally.

1. Clone the Repository

Bash:
git clone https://github.com/YOUR_USERNAME/todo_project.git
cd todo_project

2. Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

Windows:

Bash
python -m venv venv
venv\Scripts\activate

Mac/Linux:

Bash
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

Bash
pip install -r requirements.txt

🏃‍♂️ Running the Application
Start the development server using Uvicorn:

Bash
uvicorn main:app --reload
Web Interface: Open your browser and navigate to http://127.0.0.1:8000/

API: Access the raw API data at http://127.0.0.1:8000/api/tasks

📖 API Documentation
FastAPI automatically generates interactive API documentation.

Swagger UI: Navigate to http://127.0.0.1:8000/docs
Allows you to test endpoints (GET, POST) directly from the browser.

ReDoc: Navigate to http://127.0.0.1:8000/redoc
Alternative documentation format.

API Endpoints Overview
Method	Endpoint	Description	Request Body
GET	/api/tasks	Retrieve a list of all tasks.	N/A
POST	/api/tasks	Create a new task.	JSON: {"title": "...", "description": "...", "status": boolean}

🧪 Testing
This project uses pytest for automated testing of API endpoints.

To run the tests:

Bash
pytest
Tests are located in test_main.py and cover both the API response status codes and data validation.

📂 Project Structure
Plaintext
todo_project/
├── main.py              # Application entry point and route logic
├── database.py          # Database connection configuration
├── models.py            # SQLAlchemy database models
├── schemas.py           # Pydantic models for data validation
├── test_main.py         # Automated API tests
├── templates/           # HTML templates for the frontend
│   ├── base.html
│   ├── index.html
│   └── add_task.html
└── requirements.txt     # Python dependencies

☁️ Deployment
This application is ready for deployment on platforms like Render or Heroku.

Deployment Notes

Database: This application uses SQLite. On ephemeral file systems (like Render's free tier), the database file (todos.db) will be reset if the server restarts or redeploys. For production environments requiring data persistence, it is recommended to switch the database connection string in database.py to a PostgreSQL instance.

👤 Author
Sanchit Rawat

GitHub: https://github.com/SanchitRawat19

Date: 29/12/2025
