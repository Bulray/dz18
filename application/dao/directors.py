from typing import Dict, Any
from library.dao import BaseDAO


class DirectorsDAO(BaseDAO):
    def __init__(self, session):
        self.session = session