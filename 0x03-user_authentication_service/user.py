#!/usr/bin/env python3
"""Module creates an Sql model"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class User(Base):
    """Class Creates an SQL model named user for the users database"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(Integer, nullable=True)
    reser_token = Column(Integer, nullable=True)
