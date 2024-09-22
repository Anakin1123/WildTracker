from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
zxc = FastAPI()

zxc.mount("/static", StaticFiles(directory="static"), name="static")
# Инициализируем Jinja2Templates с директорией templates
templates = Jinja2Templates(directory="templates")

@zxc.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@zxc.get("/about")
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@zxc.get("/contact")
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@zxc.get("/post")
async def post(request: Request):
    return templates.TemplateResponse("post.html", {"request": request})