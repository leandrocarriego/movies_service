import logging
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.Movie import Movie
from app.schemas.Movie import CreateMovieSchema, MovieResponse

router = APIRouter()


@router.get("/")
def index():
    return {"service": "Movies service"}


@router.get("/movies", response_model=list[MovieResponse])
def get_movies(ids: list[int] = Query(None), db: Session = Depends(get_db)):
    try:
        if ids:
            movies = db.query(Movie).filter(Movie.id.in_(ids)).all()
        else:
            movies = db.query(Movie).all()
        return movies
    except Exception as e:
        logging.error(f"Error getting movies: {e}")
        raise e


@router.post("/movies", response_model=MovieResponse, status_code=201)
def create_movie(
    request: CreateMovieSchema, db: Session = Depends(get_db)
) -> MovieResponse:
    try:
        movie = Movie(title=request.title)
        db.add(movie)
        db.commit()
        db.refresh(movie)
        return movie
    except Exception as e:
        logging.error(f"Error creating movie: {e}")
        raise e


@router.delete("/movies/{movie_id}", status_code=204)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    try:
        movie = db.query(Movie).filter(Movie.id == movie_id).first()
        if movie:
            db.delete(movie)
            db.commit()
            return {"message": "Movie deleted successfully"}
        else:
            return {"message": "Movie not found"}, 404
    except Exception as e:
        logging.error(f"Error deleting movie: {e}")
        raise e
