from typing import List

from pydantic import BaseModel
from pydantic import constr
from pydantic import EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    name: str
    last_name: str
    password: str


class User(UserBase):
    id: int
    name: str
    last_name: str

    class Config:
        orm_mode = True


class PlayerGame(BaseModel):
    movimientos: List[constr(max_length=5)]
    golpes: List[constr(max_length=1)]


class Superpower(BaseModel):

    id: int
    name: str
    sequence: str
    damage: int
    character = int


class Character(BaseModel):
    id: int
    name: str
    superpowers: List[Superpower]


class Fight(BaseModel):
    id: int
    player1_game: str
    player2_game: str
    _story: str
