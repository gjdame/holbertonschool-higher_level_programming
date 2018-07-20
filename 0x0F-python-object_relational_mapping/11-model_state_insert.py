#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

def main(argv):

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    new = State(name="Louisiana")
    session.add(new)
    session.commit()
    for state in session.query(State).filter(State.name == "Louisiana").order_by(State.id).all():

        print("{}".format(state.id))
    session.close()

if __name__ == "__main__":
    import sys
    main(sys.argv)
