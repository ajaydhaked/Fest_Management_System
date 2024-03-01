from typing import Annotated
from starlette.templating import Jinja2Templates
from fastapi import FastAPI,status,Depends,Form,HTTPException
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from models.allmodels import Student,Event
from fastapi.responses import RedirectResponse
import starlette.status as status
from fastapi.security import OAuth2PasswordBearer
from database.connect import conn
from typing import List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from auth.userauth import *
from routes.admin import *

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
    cur=conn.cursor()
    cur.execute(f"INSERT INTO A4_student (name,username,roll_number,password,onlystudent) VALUES ('{student.name}', '{student.username}','{student.rollno}','{student.password}','{student.only_student}')")
    cur.close()
    conn.commit()
    conn.close() 
    return

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,"page":"home"})

@app.get("/events")
async def read_root(request: Request):
    if(request.cookies.get("username") is None):
        return RedirectResponse(url="/login?message=please login to see events page",status_code=status.HTTP_302_FOUND)
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM A4_event")
    events = cur.fetchall()
    cur.close()
    for i in range(len(events)):
        events[i] = Event(event_id=events[i][0],name=events[i][1],date=events[i][2].strftime("%d-%m-%Y"),type=events[i][3],description=events[i][4])
    return templates.TemplateResponse("events.html", {"request": request, "events": events,"page":"events"})

@app.get("/about")
async def read_root(request: Request):
    return templates.TemplateResponse("about.html", {"request": request,"page":"about"})

@app.get("/login")
async def read_root(request: Request,message: str = None):
    print(message)
    print(request.headers.get("message"))
    if request.headers.get("message"):
        message = request.headers.get("message")
    return templates.TemplateResponse("login.html", {"request": request,"page":"login","message":message})

@app.post("/loginuser")
async def read_root(request: Request,username:str=Form(...),password:str=Form(...)):
    print(username,password)
    return RedirectResponse(url="/events",status_code=status.HTTP_302_FOUND,headers={"Set-Cookie":f"token={username};"})

@app.get("/admin")
async def read_root(request: Request):
    cur = conn.cursor()
    # get all table names
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    tables = cur.fetchall()
    for i in range(len(tables)):
        cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{tables[i][0]}'")
        temp1 = cur.fetchall()
        temp1 = [x[0] for x in temp1]
        print(temp1)
        cur.execute(f"SELECT * FROM {tables[i][0]}")
        temp2 = cur.fetchall()
        tables[i]=(tables[i][0],temp1,temp2)
    return templates.TemplateResponse("/admin/admin.html", {"request": request,"tables":tables,"page":"admin"})
