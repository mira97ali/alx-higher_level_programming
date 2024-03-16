#!/usr/bin/python3
"""Model City Fetch By State"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    CONNECTION = 'mysql+mysqldb://%s:%s@localhost:3306/%s'
    engine = create_engine(CONNECTION % (username, password, database))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(
        State.name, City.id, City.name
    ).filter(State.id == City.state_id)
    for instance in query:
        print(instance[0] + ": (" + str(instance[1]) + ") " + instance[2])
