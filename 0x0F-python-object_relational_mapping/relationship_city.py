#!/usr/bin/python3
"""lass definition of a State and an instance Base = declarative_base()"""
from sqlalchemy import ForeignKey, Integer, String, Column
from relationship_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """cities class"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __repr__(self):
        return("<City(id='%s', name='%s', state_id='%s')>"
               % (self.id, self.name, self.state_id))
