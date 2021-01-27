from flask import jsonify


def rectangle_serializer(rectangles):
    response = []
    fields = ['x', 'y', 'width', 'height', 'time']
    for rectangle in rectangles:
        response.append({key: str(getattr(rectangle, key)) for key in fields})
    json_response = jsonify(response)
    return json_response
