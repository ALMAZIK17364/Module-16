from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
async def root():
    return "Главная страница"

@app.get("/user/admin")
async def admin_page():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def join_account(
    user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")]) -> dict:
    return {"Вы вошли как пользователь № ": user_id}

@app.get("/user/{username}/{age}")
async def user_info(
    username: Annotated[str, Path(min_length=5, max_length=20, title="Enter username")],
    age: Annotated[int, Path(ge=18, le=120, title="Enter age")]) -> dict:
    return {"Информация о пользователе Имя ": username, "Возраст ": age}