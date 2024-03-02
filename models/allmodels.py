from pydantic import BaseModel


class Student(BaseModel):
    name: str
    username: str
    rollno: str
    password: str
    only_student: int

class frontenduser(BaseModel):
    is_logged_in: int
    username: str
    is_organiser: int
    is_student: int
    is_outsider: int
    participate_events: list
    voluteer_events: list

class Event(BaseModel):
    event_id: int = None
    name: str
    date: str
    type: str
    description: str

class Organiser_l(BaseModel):
    unsername: str
    name: str
    password: str
    verified_password: str
    roll_no: str
    roll_name: str
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
    roll_no: str
    branch: str


class User_l(BaseModel):
    username: str
    password: str
