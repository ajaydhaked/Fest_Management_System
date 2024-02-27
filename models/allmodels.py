from pydantic import BaseModel

class Student(BaseModel):
    id:int=None
    name:str
    username:str
    rollno:str
    password:str=None
    only_student:int