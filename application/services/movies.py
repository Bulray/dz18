from typing import Dict, Any
from application.dao.movies import MoviesDAO
from application.services.schemas.movie import MovieSchema
from library.service import BaseService


class MoviesService(BaseService):
    def get_by_director_id(self, director_id: int):
      return self.schema.dump(self.dao.get_by_director_id(director_id), many=True)


    def get_by_genre_id(self, genre_id: int):
        return self.schema.dump(self.dao.get_by_genre_id(genre_id), many = True)

