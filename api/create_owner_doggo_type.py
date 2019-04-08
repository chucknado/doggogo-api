import json

import sunshine


key = 'owner_has_many_doggos'
source = 'zen:user'
target = ['doggo']

response = sunshine.create_relationship_type(key, source, target)
if response:
    print(f'\nSuccessfully created the {key} relationship type.\n')
    print(json.dumps(response, indent=2, sort_keys=True) + '\n')
