from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import api_router
from app.core.config import settings
from app.websocket import websocket_router

app = FastAPI(
    title="Security Management API",
    version="1.0.0"
)

# Configurar CORS
# Configurar middlewares
# Incluir rotas
# Configurar WebSocket
