import requests


credentials = 'your_zendesk_email', 'your_zendesk_password'
zendesk = 'https://your_subdomain.zendesk.com'


def create_object_type(key, schema):
    data = {'data': {'key': key, 'schema': schema}}
    url = f'{zendesk}/api/sunshine/objects/types'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    response = requests.post(url, json=data, auth=credentials, headers=headers)
    if response.status_code != 201:
        print(f'\nFailed to create {key} object type with error {response.status_code}: {response.text}')
        return False
    return response.json()['data']


def create_relationship_type(key, source, target):
    data = {'data': {'key': key, 'source': source, 'target': target}}
    url = f'{zendesk}/api/sunshine/relationships/types'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    response = requests.post(url, json=data, auth=credentials, headers=headers)
    if response.status_code != 201:
        print(f"\nFailed to create {key} relationship type with error {response.status_code}: {response.text}")
        return False
    return response.json()['data']


def create_object_record(obj_type, attributes):
    data = {'data': {'type': obj_type, 'attributes': attributes}}
    url = f'{zendesk}/api/sunshine/objects/records'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    response = requests.post(url, json=data, auth=credentials, headers=headers)
    if response.status_code != 201:
        return {'error_code': response.status_code}
    return response.json()['data']


def create_relationship_record(rel_type, source, target):
    data = {'data': {'relationship_type': rel_type, 'source': f'zen:user:{source}', 'target': target}}
    url = f'{zendesk}/api/sunshine/relationships/records'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    response = requests.post(url, json=data, auth=credentials, headers=headers)
    if response.status_code != 201:
        return {'error_code': response.status_code}
    return response.json()['data']


def list_related_object_records(record_id, rel_type):
    url = f'{zendesk}/api/sunshine/objects/records/{record_id}/related/{rel_type}'
    headers = {'Accept': 'application/json'}
    response = requests.get(url, auth=credentials, headers=headers)
    if response.status_code != 200:
        return {'error_code': response.status_code}
    return response.json()['data']


def update_object_record(record_id, attributes):
    url = f'{zendesk}/api/sunshine/objects/records/{record_id}'
    data = {'data': {'attributes': attributes}}
    headers = {'Content-Type': 'application/merge-patch+json', 'Accept': 'application/json'}
    response = requests.patch(url, json=data, auth=credentials, headers=headers)
    if response.status_code != 200:
        return {'error_code': response.status_code}
    return response.json()['data']
