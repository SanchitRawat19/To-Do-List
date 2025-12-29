from fastapi import FastAPI, Depends, Request, Form, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine

"""Create Table"""
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="To-Do List API Assignment")
templates = Jinja2Templates(directory="templates")

"""DB Session"""
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/tasks", response_model=schemas.TaskResponse)
def create_task_api(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """API endpoint to create a new task."""
    new_task = models.Task(title=task.title, description=task.description, status=task.status)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.get("/api/tasks", response_model=list[schemas.TaskResponse])
def read_tasks_api(db: Session = Depends(get_db)):
    """API endpoint to retrieve all tasks."""
    return db.query(models.Task).all()

@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    """Render the list of tasks."""
    tasks = db.query(models.Task).all()
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@app.get("/add")
def add_task_form(request: Request):
    """Render the form to add a task."""
    return templates.TemplateResponse("add_task.html", {"request": request})

@app.post("/add")
def add_task_submit(
    title: str = Form(...),
    description: str = Form(None),
    db: Session = Depends(get_db)
):
    """Handle form submission and redirect to home."""
    new_task = models.Task(title=title, description=description)
    db.add(new_task)
    db.commit()
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/update/{task_id}")
def update_task_status(task_id: int, db: Session = Depends(get_db)):
    """Toggle task status to True (Completed)"""
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        task.status = True
        db.commit()
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)