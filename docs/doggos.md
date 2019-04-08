## Doggos

### JSON format

| Name        | Type    | Mandatory | Comment
| ----------- | ------- | --------- | -------
| pet_owner   | integer | yes       | Zendesk user id of the dog owner. Writable only on create
| name        | string  | yes       | Dog's name
| breed       | string  | no        | Dog's breed
| birthday    | string  | no        | Known or estimated birthday in the YYYY-MM-DD format
| conditions  | string  | no        | Health issues, if any
| training    | boolean | no        | Whether the dog received obedience training
| temperament | string  | no        | Natural predisposition. Possible values: "calm", "confident", "energetic", "aggressive", "couch potato"
| strangers   | string  | no        | Attitude with strangers. Possible values: "affectionate", "reserved", "fearful"

#### Example

```json
{
  "pet_owner": 5422234,
  "name": "Soy",
  "breed": "Mix",
  "birthday": "2018-03-15",
  "conditions": "Hip dysplasia",
  "training": false,
  "temperament": "calm",
  "strangers": "reserved"
}
```

### Create Doggo

`POST /api/doggos`

Adds a doggo to a specified pet owner.

Identify the pet owner by their Zendesk user id. See [Search Users](https://developer.zendesk.com/rest_api/docs/support/users#search-users) in the Zendesk Support API docs.

#### Using cURL

```bash
curl https://doggogo.com/api/doggos \
  -d '{"doggo": {"pet_owner": 44325454, "name": "Buddy", "breed": "Black Lab", "birthday": "2018-03-15", "conditions": "None", "training": false, "temperament": "confident", "strangers": "affectionate"}}' \
 -H "Content-Type: application/json" \
 -v -X POST
```

#### Example response

```json
Status: 201 Created

{
  "name": "Buddy",
  "breed": "Black Lab",
  "birthday": "2018-03-15",
  "conditions": "None",
  "training": false,
  "temperament": "confident",
  "strangers": "affectionate"
}
```

### List Doggos

`POST /api/owners/{user_id}/doggos`

Lists a pet owner's doggos.

#### Using cURL

```bash
curl https://doggogo.com/api/owners/44325454/doggos
```

#### Example response

```json
Status: 200 OK

{
  "doggos": [
    {
      "type": "doggo",
      "id": "df8172f5-54bf-11e9-86ca-d5d3fd51aa19",
      "external_id": null,
      "attributes": {
        "name": "Buddy",
        "breed": "",
        "birthday": "2018-03-15",
        "conditions": "None",
        "training": false,
        "temperament": "confident",
        "strangers": "affectionate"
      },
      "created_at": "2019-04-01T20:51:07.680Z",
      "updated_at": "2019-04-01T20:51:08.000Z"
    }
  ]
}
```

### Update Doggo

`PUT /api/doggos/{doggo_id}`

Updates the attributes of the specified doggo record. See List Doggos.

The pet owner cannot be updated.

#### Using cURL

```bash
curl https://doggogo.com/api/doggos/df8172f5-54bf-11e9-86ca-d5d3fd51aa19 \
  -d '{"doggo": {"birthday": "2018-04-15", "conditions": "Fleas"}}' \
  -X PUT -H "Content-Type: application/json"
```

#### Example response

```json
Status: 200 Updated

{
  "name": "Buddy",
  "breed": "Black Lab",
  "birthday": "2018-04-15",
  "conditions": "Fleas",
  "training": false,
  "temperament": "confident",
  "strangers": "affectionate"
}
```
