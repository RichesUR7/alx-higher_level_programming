#!/usr/bin/python3
'''
All states via SQLAlchemy
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

    for state in session.query(State).order_by(State.id):
        print('{}: {}'.format(state.id, state.name))
    session.close()
