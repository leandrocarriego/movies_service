from typing import Union

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.routes import movies_router
from app.core.config import settings
from app.core.database import get_db, init_db

app = FastAPI(title="Movies Service")

app.dependencies=[Depends(get_db)]

app.include_router(movies_router, prefix="/api/v1" )

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.ALLOW_ORIGINS],
    allow_credentials=settings.ALLOW_CREDENTIALS,
    allow_methods=[settings.ALLOW_METHODS],
    allow_headers=[settings.ALLOW_HEADERS],
)

if __name__ == "__main__":
    import uvicorn
    
    config = uvicorn.Config(app)
    server = uvicorn.Server(config)
    server.run()
