from sqlalchemy.orm import Session
from app.models.Movie import Movie


class MovieRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_movie(self, title: str):
        movie = Movie(title=title)
        self.db.add(movie)
        self.db.commit()
        self.db.refresh(movie)
        return movie

    def delete_movie(self, movie_id: int):
        movie = self.db.query(Movie).filter(Movie.id == movie_id).first()
        if movie:
            self.db.delete(movie)
            self.db.commit()
            return True
        return False

    def get_all_movies(self):
        return self.db.query(Movie).all()

    def get_movies_by_id(self, ids: list[int] = None):
        return self.db.query(Movie).filter(Movie.id.in_(ids)).all()
