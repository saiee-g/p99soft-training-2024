from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from pydantic import BaseModel


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")

class User(BaseModel):
    username: str
    email: str | None = None
    name: str | None = None
    disbled: bool | None = None

def fake_token(token):
    return User(
        username=token, email="e@mail.com", name="Ada"
    )

def get_curr_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_token(token)
    return user

@app.get("/")
def read_user(curr_user: Annotated[User, Depends(get_curr_user)]):
    return curr_user