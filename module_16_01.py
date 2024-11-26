from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Главная страница"}


@app.get("/users/admin")
async def admin():
    return {"message": "Вы вошли как администратор"}


@app.get("/users/{user_id}")
async def user(user_id: int):
    return {"message": f"Вы вошли как пользователь {user_id}"}


@app.get("/user")
async def users_info(username: str, age: int):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
