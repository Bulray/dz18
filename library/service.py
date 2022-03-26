from typing import Dict, Any
from marshmallow import Schema
from library.dao import BaseDAO


class BaseService():
        def __init__(self, dao: BaseDAO, schema: Schema):
            self.dao = dao
            self.schema = schema

        def get_all(self):

            return self.schema.dump(self.dao.get_all(), many=True)

        def get_one(self, uid: int):
            return self.schema.dump(self.dao.get_one(uid))

        def create(self, data: Dict[str, Any]):
            return self.dao.create(data=self.schema.load(data))

        def update(self, uid: int, data: Dict[str, Any]):
            self.dao.update(uid, self.schema.load(data))


        def delete(self, uid: int):
            self.dao.delete(uid, self.schema.load(data))
