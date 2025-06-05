from fastapi import FastAPI

app = FastAPI(title="AppGini FastAPI Extension", version="0.1.0")

@app.get("/")
async def read_root():
    return {"message": "Bienvenido a la API extendida de AppGini"}

# Import and include the main API router
from app.api.api_v1.api import api_router as api_v1_router

app.include_router(api_v1_router, prefix="/api/v1")

# Aquí se montarán los routers de la API más adelante # This comment can be removed or kept
