from fastapi import FastAPI

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/")
async def root():
    return "Главная страница"

@app.get('/users')
def get_users():
    return users

@app.post('/user/{username}/{age}')
def create_user(username: str, age: int):
    new_id = str(max(map(int, users.keys())) + 1)
    users[new_id] = f'Имя: {username}, возраст: {age}'
    return f"User  {new_id} is registered"

@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: str, username: str, age: int):
    if user_id in users:
        users[user_id] = f'Имя: {username}, возраст: {age}'
        return f"The user {user_id} is updated"
    else:
        return f"User  {user_id} not found", 404

@app.delete('/user/{user_id}')
def delete_user(user_id: str):
    if user_id in users:
        del users[user_id]
        return f"User  {user_id} has been deleted"
    else:
        return f"User  {user_id} not found", 404