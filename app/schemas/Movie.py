from pydantic import BaseModel
from typing import List


class CreateMovieSchema(BaseModel):
    title: str


class MovieResponse(BaseModel):
    id: int
    title: str

