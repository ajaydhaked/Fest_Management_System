from starlette.templating import Jinja2Templates
from fastapi import FastAPI,status
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles

import psycopg2

from typing import List
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

class Student(BaseModel):
    id:int=None
    name:str
    username:str
    rollno:int
    password:str=None
    only_student:int

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.post("/student",status_code=status.HTTP_201_CREATED)
async def new_student(student:Student):
    conn=psycopg2.connect(
        database="21CS10033",user="21CS10033",password="21CS10033",host="10.5.18.68"
    )
    cur=conn.cursor()
    cur.execute(f"INSERT INTO A4_student (name,username,rollno,password,only_student) VALUES ('{student.name}', '{student.username}','{student.rollno}','{student.password}','{student.only_student}')")

    cur.close()
    conn.commit()
    conn.close() 
    return

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/events")
def read_root(request: Request):
    return templates.TemplateResponse("events.html", {"request": request})

@app.get("/about")
def read_root(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
