from starlette.templating import Jinja2Templates
from fastapi import FastAPI,status
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from models.allmodels import Student

import psycopg2

from typing import List
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware


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
conn=psycopg2.connect(
        database="21CS10033",user="21CS10033",password="21CS10033",host="10.5.18.68"
    )

@app.post("/student",status_code=status.HTTP_201_CREATED)
async def new_student(student:Student):
   
    cur=conn.cursor()
    cur.execute(f"INSERT INTO A4_student (name,username,roll_number,password,onlystudent) VALUES ('{student.name}', '{student.username}','{student.rollno}','{student.password}','{student.only_student}')")
    cur.close()
    conn.commit()
    conn.close() 
    return


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/events")
def read_root(request: Request):
    cur = conn.cursor()
    cur.execute("SELECT * FROM A4_event")
    events = cur.fetchall()
    print(events)
    return templates.TemplateResponse("events.html", {"request": request})

@app.get("/about")
def read_root(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

