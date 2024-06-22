from pydantic import BaseModel


class Student(BaseModel):
    name: str
    username: str
    rollno: str
    password: str
    only_student: int

class frontenduser(BaseModel):
    is_logged_in: int
    username: str|None
    is_organiser: int
    is_student: int
    is_outsider: int
    participate_events: list
    volunteer_events: list

class profile(BaseModel):
    name: str
    username: str
    rollno: str
    collegename: str
    merchtaken: int
    rolename: str
    roledesc: str

class Event(BaseModel):
    event_id: int = None
    name: str
    date: str
    type: str
    description: str
    winner_declared: int
    winners: list

class Organiser_l(BaseModel):
    username: str
    name: str
    password: str
    roll_no: str
    enrollment_key: str

class Student_l(BaseModel):
    username: str
    name: str
    password: str
    roll_no: str

class Outsider_l(BaseModel):
    username: str
    name: str
    password: str
    college: str


class User_l(BaseModel):
    username: str
    password: str
