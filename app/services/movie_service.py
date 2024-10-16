# app/services/movie_service.py

import logging
from sqlalchemy.orm import Session
from app.repositories.movie_repository import MovieRepository
from app.schemas.Movie import MovieResponse


class MovieService:
    def __init__(self, db: Session):
        self.repository = MovieRepository(db)

    def create_movie(self, title: str):
        try:
            return self.repository.create_movie(title)
        except Exception as e:
            logging.error(f"Error creating movie: {e}")
            raise e

    def delete_movie(self, movie_id: int):
        try:
            return self.repository.delete_movie(movie_id)
        except Exception as e:
            logging.error(f"Error deleting movie: {e}")
            raise e

    def get_all_movies(self) -> list[MovieResponse]:
        try:
            movies = self.repository.get_all_movies()
            return [MovieResponse(id=movie.id, title=movie.title) for movie in movies]
        except Exception as e:
            logging.error(f"Error fetching all movies: {e}")
            raise e

    def get_movies_by_id(self, ids: list[int]) -> list[MovieResponse]:
        try:
            movies = self.repository.get_movies_by_id(ids)
            return [MovieResponse(id=movie.id, title=movie.title) for movie in movies]
        except Exception as e:
            logging.error(f"Error fetching movies by id: {e}")
            raise e
