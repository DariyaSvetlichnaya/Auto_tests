from marshmallow import Schema, fields, post_load

from dataclasses import dataclass

import json


@dataclass
class CategoriesDTO:
    id: int
    name: str


@dataclass
class TagsDTO:
    id: int
    name: str


@dataclass
class PetsDTO:
    id: int
    category: dict[CategoriesDTO]
    name: str
    photoUrls: list
    tags: list[TagsDTO]
    status: str


class CategoriesSchema(Schema):
    id = fields.Integer(required=True, strict=True)
    name = fields.Str(required=True)

    @post_load
    def serialize(self, data, **kwarg):
        return CategoriesDTO(**data)


class TagsSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.Str(required=True)

    @post_load
    def serialize(self, data, **kwarg):
        return TagsDTO(**data)


class PetsSchema(Schema):
    id = fields.Integer(required=True)
    category = fields.Nested(CategoriesSchema, required=True)
    name = fields.Str(required=True)
    photoUrls = fields.List(fields.Str(), required=True)
    tags = fields.Nested(TagsSchema, many=True, required=True)
    status = fields.Str(required=True)

    @post_load
    def serialize(self, data, **kwarg):
        return PetsDTO(**data)


if __name__ == '__main__':
    with open('pets.json') as pets_json:
        data = json.load(pets_json)

    pets_dto = PetsSchema(many=True).load(data)

    for pet in pets_dto:
        tags = [tag.name for tag in pet.tags]
        print(pet.name, pet.category.name, tags)
