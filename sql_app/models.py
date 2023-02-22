from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy.orm import validates
from sqlalchemy.schema import CheckConstraint

from sql_app.base_class import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class Character(Base):
    __tablename__ = "character"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    last_name = Column(String)

    def get_superpowers(self, db: Session):
        return db.query(Superpower).filter(Superpower.character == self.id)


class Superpower(Base):
    __tablename__ = "superpower"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    sequence = Column(String)
    damage = Column(Integer)
    character = Column(Integer, ForeignKey("character.id"))

    # __table_args__ = (
    #     CheckConstraint('char_length(sequence) >= 3',
    #                     name='sequence_min_length'),
    #     CheckConstraint('char_length(sequence) <= 6',
    #                     name='sequence_max_length'),
    # )

    @validates("sequence")
    def validate_some_string(self, key, sequence) -> str:
        if len(sequence) < 3:
            raise ValueError("sequence too short")
        if len(sequence) > 6:
            raise ValueError("sequence too large")
        return sequence


class Fight(Base):
    __tablename__ = "fight"

    id = Column(Integer, primary_key=True, index=True)
    player1_game = Column(String)
    player2_game = Column(String)
    winner = Column(String)
    _story = Column(String)

    @property
    def story(self):
        return self._story.split(";")
