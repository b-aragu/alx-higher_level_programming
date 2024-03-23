#!/usr/bin/python3
'''Class city'''

from sqlalchemy import Integer, String, Column, ForeignKey
from model_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    '''class city'''
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
