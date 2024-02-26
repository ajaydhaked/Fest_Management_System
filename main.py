from starlette.templating import Jinja2Templates
from fastapi import FastAPI
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/events")
def read_root(request: Request):
    return templates.TemplateResponse("events.html", {"request": request})

@app.get("/about")
def read_root(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
