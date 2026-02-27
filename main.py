from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

# DB
from app.db.database import connect_to_db, disconnect_from_db

# Routes
from app.routes.auth_routes import router as auth_router
from app.routes.task_routes import router as task_router


# -------------------------------
# Logging Configuration
# -------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# -------------------------------
# Lifespan (Startup / Shutdown)
# -------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_db()
    logger.info("Database connected")
    yield
    await disconnect_from_db()
    logger.info("Database disconnected")


app = FastAPI(lifespan=lifespan)


# -------------------------------
# Global Exception Handlers
# -------------------------------

# Handle HTTPException separately (optional but clean)
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "detail": exc.detail,
        },
    )


# Handle all unhandled exceptions
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}", exc_info=True)

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "detail": "Internal Server Error",
        },
    )


# -------------------------------
# Routers
# -------------------------------
app.include_router(auth_router)
app.include_router(task_router)


# -------------------------------
# CORS
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)