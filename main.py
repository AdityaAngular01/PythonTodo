from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.database import connect_to_db, disconnect_from_db
from fastapi.middleware.cors import CORSMiddleware

# Routes
from app.routes.auth_routes import router as auth_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_db()
    yield
    await disconnect_from_db()

app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)