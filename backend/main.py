from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes.auth import auth_router
from src.routes.gallery import gallery_router
from src.routes.photo import photo_router
from src.routes.profile import profile_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(gallery_router)
app.include_router(photo_router)
app.include_router(profile_router)
