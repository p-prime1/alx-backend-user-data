#!/usr/bin/env python2
"""Module creates an Sql model"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class User(Base):
    """Class Creates an SQL model named user for the users database"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    hashed_password = Column(String)
    session_id = Column(Integer)
    reser_token = Column(Integer)
