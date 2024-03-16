#!/usr/bin/python3
"""Model State Insert"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    CONNECTION = 'mysql+mysqldb://%s:%s@localhost:3306/%s'
    engine = create_engine(CONNECTION % (username, password, database))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    STATE_NAME = 'Louisiana'
    session.add(State(name=STATE_NAME))
    new_instance = session.query(State).filter_by(name=STATE_NAME).first()
    print(new_instance.id)
    session.commit()
