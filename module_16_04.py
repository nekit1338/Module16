import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app_01 = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app_01.get('/users')
async def get_users() -> list[User]:
    return users


@app_01.post('/user/{username}/{age}')
async def create_user(
        username: str,
        age: int
) -> User:
    if len(users) == 0:
        new_user = User(id=1, username=username, age=age)
        users.append(new_user)
        return new_user
    if len(users) >= 1:
        new_user = User(id=users[-1].id + 1, username=username, age=age)
        users.append(new_user)
        return new_user


@app_01.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: int,
        username: str,
        age: int,
) -> User:
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = User(id=user_id, username=username, age=age)
            return users[index]
    raise HTTPException(status_code=404, detail="User was not found")


@app_01.delete('/user/{user_id}')
async def delete_user(
        user_id: int
) -> list:
    for index, user in enumerate(users):
        if user.id == user_id:
            users.pop(index)
            return users
    raise HTTPException(status_code=404, detail="User was not found")


if __name__ == '__main__':
    uvicorn.run(app_01, host='127.0.0.1', port=8000)
