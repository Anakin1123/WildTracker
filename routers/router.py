from fastapi import APIRouter

# Создание экземпляра маршрутизатора
router = APIRouter()

# Пример маршрута
@router.get("/example")
async def example():
    return {"message": "Hello from the example route!"}
