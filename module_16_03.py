from typing import Annotated
import uvicorn
from fastapi import FastAPI, Path

app_01 = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app_01.get('/users')
async def get_users() -> dict:
    return users


@app_01.post('/user/{username}/{age}')
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
        age: Annotated[int, Path(gt=18, le=120, description="Enter age")]
) -> str:
    max_user_id = int(max(users.keys())) + 1
    users[str(max_user_id)] = f"Имя: {username}, возраст: {age}"
    return f"User {max_user_id} is registered"


@app_01.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(gt=0)],
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
        age: Annotated[int, Path(gt=18, le=120, description="Enter age")]
) -> str:
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app_01.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(gt=0)]
) -> str:
    del users[str(user_id)]
    return f"User {user_id} is deleted"

if __name__ == '__main__':
    uvicorn.run(app_01, host='127.0.0.1', port=8000)