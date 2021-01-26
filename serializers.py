from flask import jsonify


def rectangle_serializer(rectangles):
    response = []
    for rectangle in rectangles:
        fields = ['x', 'y', 'width', 'height', 'time']
        response.append({key: str(getattr(rectangle, key)) for key in fields})
    json_response = jsonify(response)
    return json_response
