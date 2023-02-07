from forum.database import Base
from sqlalchemy import Column, String, Integer, Text, DateTime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    email = Column(String)
    password = Column(String)
