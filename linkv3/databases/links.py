from models import Link,db
from connexion import problem
from sqlalchemy.exc import SQLAlchemyError
from flask import jsonify


def healthcheck():
    try:
        db.session.execute('SELECT * from link')
    except SQLAlchemyError as e:
        return problem(500,'Database not available',detail=str(e))

    return {'result':'ok'}


def add_service(dates):
    new_link = Link(name=dates.get('name'),url=dates.get('link'))
    db.session.add(new_link)
    db.session.commit()
    return {'result' : 'success'}


def show_all(domen='', fl='', id=0):

    resp = db.session.query(Link).all()
    serialized = {}
    for i in range(0, len(resp)):
        serialized[resp[i].id] = {"name": str(resp[i].name), "url": str(resp[i].url)}

    if id > 0:
        tmp = {}
        tmp[id] = serialized.get(id)
        serialized = tmp
    if len(fl) != 0:
        tmp = {}
        for key, value in serialized.items():
            if value['name'][0] == fl:
                tmp[key] = value
        serialized = tmp
    if len(domen) != 0:
        tmp = {}
        for key, value in serialized.items():
            if value['url'].split('.')[2] == domen:
                tmp[key] = value
        serialized = tmp

    return serialized




    



