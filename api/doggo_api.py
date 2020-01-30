import json

import sunshine
from bottle import route, run, request, response


@route('/test')
def test():
    return '<p>Hello World!</p>'


@route('/api/doggos', method='POST')
def add_doggo():
    # create doggo record
    attributes = request.json.get('doggo')
    obj_type = 'doggo'
    pet_owner = attributes.pop('pet_owner')  # used in creating relationship
    if 'name' not in attributes:
        response.status = 400
        return

    doggo_record = sunshine.create_object_record(obj_type, attributes)
    if 'error_code' in doggo_record:
        response.status = doggo_record['error_code']
        return

    # create relationship record
    rel_type = 'owner_has_many_doggos'
    source = pet_owner
    target = doggo_record['id']
    relationship_record = sunshine.create_relationship_record(rel_type, source, target)
    if 'error_code' in relationship_record:
        response.status = relationship_record['error_code']
        return

    # send new doggo record in response
    response.status = 201
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'record': doggo_record})


@route('/api/owners/<user_id>/doggos')
def list_doggos(user_id):
    user_id = f'zen:user:{user_id}'
    rel_type = 'owner_has_many_doggos'
    doggos = sunshine.list_related_object_records(user_id, rel_type)
    if 'error_code' in doggos:
        response.status = doggos['error_code']
        return
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'doggos': doggos})


@route('/api/doggos/<doggo_id>', method='PUT')
def update_doggo(doggo_id):
    attributes = request.json.get('doggo')
    record = sunshine.update_object_record(doggo_id, attributes)
    if 'error_code' in record:
        response.status = record['error_code']
        return
    response.status = 200
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'record': record})


run(debug=True)
