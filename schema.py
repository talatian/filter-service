rectangle_schema = {
    'type': 'object',
    'properties':
        {
            'x': {'type': 'integer'},
            'y': {'type': 'integer'},
            'width': {'type': 'integer'},
            'height': {'type': 'integer'}
        },
    'required': ['x', 'y', 'width', 'height']
}

filter_input_schema = {
    'type': 'object',
    'properties':
        {
            'main': rectangle_schema,
            'input':
                {
                    'type': 'array',
                    'items': [rectangle_schema]
                },
        },
    'required': ['main', 'input']
}
