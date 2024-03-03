from typing import Annotated
from starlette.templating import Jinja2Templates
from fastapi import FastAPI, status, Depends, Form, HTTPException
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from models.allmodels import *
from fastapi.responses import RedirectResponse
import starlette.status as status
from fastapi.security import OAuth2PasswordBearer
from database.connect import conn
from typing import List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from psycopg2 import Error
from models.modelfunction import *
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