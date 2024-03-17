#!/usr/bin/python3
'''
prints the first State
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

    state = session.query(State).order_by(State.id).first()
    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')
    session.close()
