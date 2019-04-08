import json

import sunshine


key = 'dogggo'
schema = {
    'properties': {
        'name': {
            'type': 'string',
            'description': 'The dog\'s name'
        },
        'breed': {
            'type': 'string',
            'description': 'Dog breed'
        },
        'birthday': {
            'type': 'string',
            'description': 'Known or estimated birthday in the YYYY-MM-DD format. Example: "2015-04-16"'
        },
        'conditions': {
            'type': 'string',
            'description': 'Medical conditions, if any'
        },
        'training': {
            'type': 'boolean',
            'description': 'Whether the dog received obedience training'
        },
        'temperament': {
            'type': 'string',
            'description': 'Natural predisposition',
            'enum': ['calm', 'confident', 'energetic', 'aggressive', 'couch potato']
        },
        'strangers': {
            'type': 'string',
            'description': 'Attitude with strangers',
            'enum': ['affectionate', 'reserved', 'fearful']
        }
    },
    'required': ['name']
}
response = sunshine.create_object_type(key, schema)
if response:
    print(f'\nSuccessfully created the {key} object type.\n')
    print(json.dumps(response, indent=2, sort_keys=True) + '\n')
