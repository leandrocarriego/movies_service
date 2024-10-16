from sqlalchemy import Column, Integer, String

from ..core.database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)

    def __repr__(self):
        return f"<Movie(title={self.title})>"