from http import HTTPStatus

from fastapi import FastAPI

from fastapi_se_deep_dive.schemas import (
    Message,
    UserDB,
    UserPublic,
    UserSchema,
)

app = FastAPI()
database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def main():
    return {'message': 'Hello World'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(
        username=user.username,
        email=user.email,
        password=user.password,
        id=len(database) + 1,
    )

    database.append(user_with_id)

    return user_with_id


@app.delete('/users')
def delete_user(userDB: int):
    return
