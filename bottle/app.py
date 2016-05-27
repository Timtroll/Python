import os
HOST = os.environ.get('THOST', '127.0.0.1')

from sqlalchemy import create_engine, schema, Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgres://test:test@%s:3306/test" % HOST, pool_size=10)
metadata = schema.MetaData()
Base = declarative_base(metadata=metadata)
Session = sessionmaker(bind=engine)


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    content = Column(String(length=512))


import bottle
import requests

app = bottle.Bottle()


@app.route('/json')
def json():
    return {'message': 'Hello, World!'}


@app.route('/remote')
def remote():
    response = requests.get('http://%s' % HOST)
    return response.text


@app.route('/complete')
def complete():
    session = Session()
    messages = list(session.query(Message).all())
    messages.append(Message(content='Hello, World!'))
    messages.sort(key=lambda m: m.content)
    session.close()
    return bottle.template('template', messages=messages)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)