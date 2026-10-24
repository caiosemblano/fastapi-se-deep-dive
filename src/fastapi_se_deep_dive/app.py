from http import HTTPStatus
from fastapi import FastAPI
from fastapi_se_deep_dive.schemas import Message

app = FastAPI()


@app.get(
    '/',
    status_code=HTTPStatus.OK,
    response_model=Message
    )
def main():
    return {'message': 'Hello World'}
