from sqlalchemy import (
    Column, Integer, Text, Boolean
)

from .declarative_model import DeclarativeBase


class Girl(DeclarativeBase):
    __tablename__ = 'girls'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url_path = Column(Text(), nullable=False)
    used = Column(Boolean(), default=False)