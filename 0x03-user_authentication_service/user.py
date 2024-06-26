#!/usr/bin/env python3
''' user file - SQLAlchemy model user for DB users '''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    ''' model for db table users
    includes attributes for users '''
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __repr__(self):
        """Representation of the user instance"""
        return f'User ({self.id}): {self.email} - {self.hashed_password}'
