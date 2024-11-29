from fastapi import FastAPI
from app.routers.menu import router as menu_router

app = FastAPI()

# Registrar as rotas de menu
app.include_router(menu_router, prefix="/menu", tags=["Menu"])
