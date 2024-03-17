#!/usr/bin/python3
'''
prints the State object with the name passed as argument
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

    state = session.query(State).filter(State.name == argv[4]).first()
    print('Not found' if not state else state.id)
    session.close()
