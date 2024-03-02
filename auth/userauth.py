from typing import Annotated
from fastapi import FastAPI,status,Depends,HTTPException
from starlette.requests import Request
from models.allmodels import Student,Event
from database.connect import conn
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import RedirectResponse
from typing import List
from pydantic import BaseModel
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM A4_student WHERE username='{token}'")
    user = cur.fetchone()
    cur.close()
    if(user is None):
        return None
    user = Student(user[0],user[1],user[2],user[3],user[4],user[5],user[6],user[7])
    return user

    
