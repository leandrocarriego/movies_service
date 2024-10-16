from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def index():
    return {"endpoint": "Movies service"}


@router.get("/movies")
def get_movies():
    return {"endpoint": "get_movies"}

@router.post("/movies")
def create_movie():
    return {"endpoint": "create_movie"}

@router.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    return {"endpoint": "delete_movie"}
