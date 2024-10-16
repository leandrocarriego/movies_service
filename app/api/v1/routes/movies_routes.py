import logging
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.Movie import Movie
from app.schemas.Movie import CreateMovieSchema, MovieResponse
from app.services.movie_service import MovieService

router = APIRouter()


@router.get("/")
def index():
    return {"service": "Movies service"}


@router.get("/movies", response_model=list[MovieResponse])
def get_movies(ids: list[int] = Query(None), db: Session = Depends(get_db)):
    service = MovieService(db)
    if ids:
        movies = service.get_movies_by_id(ids)
    else:
        movies = service.get_all_movies()
    return movies


@router.post("/movies", response_model=MovieResponse, status_code=201)
def create_movie(
    request: CreateMovieSchema, db: Session = Depends(get_db)
) -> MovieResponse:
    service = MovieService(db)
    movie = service.create_movie(title=request.title)
    return movie


@router.delete("/movies/{movie_id}", status_code=204)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    service = MovieService(db)
    return service.delete_movie(movie_id)
