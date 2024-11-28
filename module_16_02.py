from typing import Annotated
import uvicorn
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def user(user_id: Annotated[int, Path(gt=1, le=100, description="Enter User ID")]) -> dict:
    return {"message": f"Вы вошли как пользователь {user_id}"}


@app.get("/user/{username}/{age}")
async def users_info(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
        age: Annotated[int, Path(gt=18, le=120, description="Enter age")]
) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
