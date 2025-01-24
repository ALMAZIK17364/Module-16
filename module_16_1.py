from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Главная страница"


@app.get("/user/admin")
async def admin_page():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def join_account(user_id: str) -> dict:
    return {"Вы вошли как пользователь № ": user_id}

@app.get("/user")
async def user_info(username: str = "Steve", age: str = 42) -> dict:
    return {"Информация о пользователе Имя ": username, "Возраст ": age}
