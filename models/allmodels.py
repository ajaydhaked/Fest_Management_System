from pydantic import BaseModel

class Student(BaseModel):
    name:str
    username:str
    rollno:str
    password:str
    only_student:int
    
    
class Event(BaseModel):
    event_id:int=None
    name:str
    date:str
    type:str
    description:str