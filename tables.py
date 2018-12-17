import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

base = declarative_base()


class Make(base):
    __tablename__ = "Make"
    id = Column(Integer, primary_key=True)
    Make = Column(String)

class Model(base):
    __tablename__ = "Model"
    id = Column(Integer, primary_key=True)
    makeid = Column(Integer, ForeignKey("Make.id"))
    make = relationship(Make)
    Model = Column(String)


class config(base):
    __tablename__ = "config"
    id = Column(Integer, primary_key=True)
    makeid = Column(Integer, ForeignKey("Make.id"))
    make = relationship(Make)
    modelid = Column(Integer, ForeignKey("Model.id"))
    model = relationship(Model)
    Year = Column(String)
    PCD = Column(String)
    Offset = Column(String)
    Bore = Column(String)
    Multi_fit_possible = Column(String)
    Hub = Column(Integer)
    PCD01 = Column(Integer)
    FitmentFrontrear = Column(String)
    Spacer = Column(String)
    Bolts = Column(String)
    THD = Column(String)
    Notes = Column(String)


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///Master-PCD.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
base.metadata.create_all(engine)
