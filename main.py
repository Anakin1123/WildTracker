from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from routers.router import router  # Импортируйте ваш маршрутизатор

# Инициализация приложения FastAPI
app = FastAPI()

# Подключение статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")

# Инициализация Jinja2Templates с директорией templates
templates = Jinja2Templates(directory="templates")

# Главная страница
@app.get("/", name='home')
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Страница "О нас"
@app.get("/about", name='about')
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

# Страница "Контакты"
@app.get("/contact",name='contact')
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

# Страница блога
@app.get("/post",name='post')
async def post(request: Request):
    return templates.TemplateResponse("post.html", {"request": request})

# Подключение маршрутизатора (если потребуется в будущем)
app.include_router(router, prefix="/api")