from numbers import Real
from fastapi import Depends, FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi_users import FastAPIUsers
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserCreate
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

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(Real, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"