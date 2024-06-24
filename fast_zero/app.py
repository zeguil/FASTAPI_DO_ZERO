from fastapi import FastAPI
from .schemas import UserPublic, UserSchema

app = FastAPI()


@app.get('/')
def reead_root():
    return {'msg': 'ola mundo'}

@app.post('/', response_model=UserPublic)
def create_user(user: UserSchema):
    return user

