#!/usr/bin/python3
"""Start link class to table in database """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main(argv):

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    new = State(name="California")
    new_c = City(name="San Francisco")
    new.cities.append(new_c)
    session.add(new)
    session.commit()

    session.close()


if __name__ == "__main__":
    import sys
    main(sys.argv)
