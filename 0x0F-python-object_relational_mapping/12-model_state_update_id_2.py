#!/usr/bin/python3
'''
Changes the name of a State object
'''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if _name_ == '_main_':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    InstanceSession = sessionmaker(bind=engine)
    session = InstanceSession()

    states = session.query(State).filter(State.id == 2)

    for el in states:
        el.name = 'New Mexico'

    session.commit()
    session.close()
