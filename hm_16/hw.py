import self
from marshmallow import Schema, fields, post_load


class CategorySchema(Schema):
    id = fields.Integer(required=True)
    name = fields.Str(required=True)


class TagSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.Str(required=True)


class PetSchema(Schema):
    id = fields.Integer(required=True)
    category = fields.Nested(CategorySchema, required=True)
    name = fields.Str(required=True)
    photoUrls = fields.List(fields.Str(), required=True)
    tags = fields.Nested(TagSchema, many=True, required=True)
    status = fields.Str(required=True)

    @post_load
    def make_pet(self, data, **kwargs):
        return Pet(**data)


class Pet:
    def __init__(self, id, category, name, photoUrls, tags, status):
        self.id = id
        self.category = category
        self.name = name
        self.photoUrls = photoUrls
        self.tags = tags
        self.status = status


if __name__ == '__main__':
    data = [
        {
            "id": 9223372036854617000,
            "category": {
                "id": 42892111,
                "name": "dolore laboris exercitation enim"
            },
            "name": "doggie",
            "photoUrls": [
                "enim do amet et",
                "in incididunt nulla"
            ],
            "tags": [
                {
                    "id": 13217034,
                    "name": "Duis in"
                },
                {
                    "id": -1050560,
                    "name": "occaecat nulla et Duis"
                }
            ],
            "status": "sold"
        },
        {
            "id": 9223372036854617000,
            "category": {
                "id": -19816953,
                "name": "officia"
            },
            "name": "doggie",
            "photoUrls": [
                "aute do",
                "aliquip"
            ],
            "tags": [
                {
                    "id": -7497000,
                    "name": "velit dolore deserunt nostrud"
                },
                {
                    "id": 61724686,
                    "name": "consequat voluptate pariatur adipisicing aliquip"
                }
            ],
            "status": "sold"
        },
        {
            "id": 56331470,
            "category": {
                "id": 28262311,
                "name": "nostrud proident"
            },
            "name": "doggie",
            "photoUrls": [
                "sunt dolor veniam aliqua",
                "nulla anim ex"
            ],
            "tags": [
                {
                    "id": 21515670,
                    "name": "voluptate in elit ani"
                },
                {
                    "id": -36858804,
                    "name": "proident non deserunt"
                }
            ],
            "status": "sold"
        },
        {
            "id": 9223372036854617000,
            "category": {
                "id": -39782949,
                "name": "consectetur in dolor"
            },
            "name": "doggie",
            "photoUrls": [
                "nostrud Excepteur",
                "in reprehenderit magna"
            ],
            "tags": [
                {
                    "id": 63823124,
                    "name": "adipisicing dolor"
                },
                {
                    "id": 87743804,
                    "name": "commodo non enim officia ipsum"
                }
            ],
            "status": "sold"
        },
        {
            "id": 3708840,
            "category": {
                "id": 9855812,
                "name": "Duis in commodo"
            },
            "name": "doggie",
            "photoUrls": [
                "minim id in sit",
                "est esse culpa nisi"
            ],
            "tags": [
                {
                    "id": -89808508,
                    "name": "sit"
                },
                {
                    "id": -5238278,
                    "name": "dolor in"
                }
            ],
            "status": "sold"
        }
    ]

    pets_schema = PetSchema(many=True)
    pets = pets_schema.load(data)

    for pet in pets:
        tags = [tag.name for tag in pet.tags]
        print(pet.name, pet.category.name, tags)
