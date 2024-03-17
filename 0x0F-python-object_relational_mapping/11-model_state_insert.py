#!/usr/bin/python3
'''
Adds the State object “Louisiana”
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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
