from application.dao.movies import MoviesDAO
from application.database import db
from application.services.movies import MoviesService
from application.services.schemas.movie import MovieSchema

movies_schema = MovieSchema
movies_dao = MoviesDAO(db.session)
movies_service = MoviesService(movies_dao, movies_schema)