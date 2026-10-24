from http import HTTPStatus

from fastapi import FastAPI

from fastapi_se_deep_dive.schemas import Message, UserSchema

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def main():
    return {'message': 'Hello World'}


@app.post('/users/', status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema):
    return user
