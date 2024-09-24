from fastapi import FastAPI, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles

# Инициализация приложения FastAPI
app = FastAPI()

# Инициализация маршрутизатора для работы со студентами
router = APIRouter(prefix='/students', tags=['Работа со студентами'])

# Подключение статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")

# Инициализация Jinja2Templates с директорией templates
templates = Jinja2Templates(directory="templates")

# Главная страница
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Страница "О нас"
@app.get("/about")
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

# Страница "Контакты"
@app.get("/contact")
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

# Страница блога
@app.get("/post")
async def post(request: Request):
    return templates.TemplateResponse("post.html", {"request": request})

# Подключение маршрутизатора (если потребуется в будущем)
app.include_router(router)