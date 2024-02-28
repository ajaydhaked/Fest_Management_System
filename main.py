from starlette.templating import Jinja2Templates
from fastapi import FastAPI,status
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from models.allmodels import Student,Event

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
        database="techfest",user="postgres",password="Ajay@123",host="localhost",port="5432"
    )
    
if conn:
    print("connected to database")
else:    
    print("not connected to database")

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
    return templates.TemplateResponse("index.html", {"request": request,"page":"home"})

@app.get("/events")
def read_root(request: Request):
    cur = conn.cursor()
    cur.execute("SELECT * FROM A4_event")
    events = cur.fetchall()
    cur.close()
    for i in range(len(events)):
        events[i] = Event(event_id=events[i][0],name=events[i][1],date=events[i][2].strftime("%d-%m-%Y"),type=events[i][3],description=events[i][4])
    return templates.TemplateResponse("events.html", {"request": request, "events": events,"page":"events"})

@app.get("/about")
def read_root(request: Request):
    return templates.TemplateResponse("about.html", {"request": request,"page":"about"})

