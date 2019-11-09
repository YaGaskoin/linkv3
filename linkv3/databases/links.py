from models import Link,db
from connexion import problem
from sqlalchemy.exc import SQLAlchemyError
from aiohttp.web_request import Request
from aiohttp.web_response import Response
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


async def show_all(request: Request):
    id = request.query.get('id')
    resp = db.session.query(Link).all().filter(Link.id == id)
    serialized = {}
    for i in range(0, len(resp)):
        serialized[str(resp[i].id)] = {"name": str(resp[i].name), "url": str(resp[i].url)}
    print(jsonify(serialized))
    return Response(text='All right!')




    



