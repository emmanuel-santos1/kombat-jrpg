from typing import List

from sqlalchemy.orm import Session

from core.hashing import Hasher
from sql_app import models
from sql_app import schemas


# --------- USER ----------
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_new_user(db: Session, user: schemas.UserCreate):
    hashed_password = Hasher.get_password_hash(user.password)
    db_user = models.User(
        name=user.name,
        last_name=user.last_name,
        email=user.email,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# --------- CHARACTER ----------
def get_character_by_name(db: Session, name: str):
    character = db.query(models.Character).filter(models.Character.name == name).first()
    return character


def get_or_create_character(db: Session, name: str, last_name: str):
    c = (
        db.query(models.Character)
        .filter(
            models.Character.name == name,
            models.Character.last_name == last_name,
        )
        .first()
    )

    if c is None:
        c = models.Character(name=name, last_name=last_name)
        db.add(c)
        db.commit()
        db.refresh(c)
    return c


# -------- SUPERPOWER ---------
def get_or_create_superpower(
    db: Session, name: str, damage: int, sequence: str, c: models.Character
):
    sp = (
        db.query(models.Superpower)
        .filter(models.Superpower.name == name, models.Superpower.character == c.id)
        .first()
    )

    if sp is None:
        sp = models.Superpower(
            name=name, damage=damage, sequence=sequence, character=c.id
        )
        db.add(sp)
        db.commit()


# ---------- FIGHT -----------
def create_fight(db: Session, p1_game: schemas.PlayerGame, p2_game: schemas.PlayerGame):
    fight = models.Fight(
        player1_game=f"Movimientos: {str(p1_game.movimientos)}, Golpes: {str(p1_game.golpes)}",
        player2_game=f"Movimientos: {str(p1_game.movimientos)}, Golpes: {str(p1_game.golpes)}",
    )
    db.add(fight)
    db.commit()
    db.refresh(fight)
    return fight


def update_fight(db: Session, figth_id: int, story: List[str], winner: str):
    figth = db.query(models.Fight).filter(models.Fight.id == figth_id).first()
    figth._story = ";".join(story)
    figth.winner = winner
    db.add(figth)
    db.commit()
    db.refresh(figth)
    return figth


def list_fights(db: Session):
    fights = db.query(models.Fight).all()
    return fights


def search_fight(query: str, db: Session):
    fights = db.query(models.Fight).filter(models.Fight.winner.contains(query))
    return fights
