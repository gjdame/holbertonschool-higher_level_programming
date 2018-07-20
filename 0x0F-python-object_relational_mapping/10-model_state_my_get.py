#!/usr/bin/python3
"""Start link class to table in database """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main(argv):

    flag = 0
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1],
                                   argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    for state in session.query(State).filter(
            State.name == argv[4]).order_by(
            State.id).all():
        if state:
            flag = 1
            print("{}".format(state.id))
    if flag == 0:
        print("Not found")
    session.close()


if __name__ == "__main__":
    import sys
    main(sys.argv)
