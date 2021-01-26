import json
from flask_expects_json import expects_json
from flask import Flask, request, Response
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from database import engine, Base
from models import Rectangle
from schema import filter_input_schema
from serializers import rectangle_serializer

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


@app.route('/', methods=['POST'])
@expects_json(filter_input_schema)
def filter_rectangles():
    json_request = json.loads(request.data)
    main = json_request['main']
    rectangles = json_request['input']
    session = Session()
    target = Rectangle(**main)
    for item in rectangles:
        rectangle = Rectangle(**item)
        if target.overlaps(rectangle):
            session.add(rectangle)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
    return Response(status=200)


@app.route('/', methods=['GET'])
def list_rectangles():
    session = Session()
    rectangles = session.query(Rectangle).all()
    response = rectangle_serializer(rectangles)
    return response


if __name__ == '__main__':
    app.run()
