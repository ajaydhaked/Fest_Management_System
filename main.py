from starlette.templating import Jinja2Templates
from fastapi import FastAPI, HTTPException
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


# Data model for different user types
class Organiser(BaseModel):
    name: str
    password: str
    verified_password: str
    roll_no: str
    roll_name: str
    enrollment_key: str


class Student(BaseModel):
    name: str
    password: str
    verified_password: str
    roll_no: str


class Outsider(BaseModel):
    name: str
    password: str
    verified_password: str
    college: str
    roll_no: str
    branch: str


user_database = {
    "swadhinsatapathy": {
        "username": "swadhinsatapathy",
        "password": "secretpassword"
    }
}


class User(BaseModel):
    username: str
    password: str


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/signup")
def v_signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


@app.get("/login")
def v_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/signup")
async def signup(request: Request):
    data = await request.json()

    if data['type'] == 'organiser':
        user = Organiser(**data)
    elif data['type'] == 'student':
        user = Student(**data)
    elif data['type'] == 'outsider':
        user = Outsider(**data)
    else:
        return {"error": "Invalid user type"}

    # Store user data (you'll likely use a database here)
    print("User Data:", user)

    return {"message": "Signup successful"}


@app.post("/login")
async def login(user: User):
    if user.username in user_database:
        stored_user = user_database[user.username]
        if stored_user["password"] == user.password:
            return {"message": "Login successful!"}

    raise HTTPException(status_code=401, detail="Invalid username or password")
