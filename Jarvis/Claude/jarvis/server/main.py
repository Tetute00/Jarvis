#!/usr/bin/env python3
"""
Punto de entrada principal para el servidor Jarvis.
Inicia el servidor FastAPI y configura todos los endpoints.
"""

import uvicorn
from fastapi import FastAPI
import json
import os

# Inicializar la aplicación FastAPI
app = FastAPI(
    title="Jarvis Server",
    description="Servidor central del sistema Jarvis",
    version="0.1.0"
)

# Cargar configuración
with open("config.json", "r") as config_file:
    config = json.load(config_file)

@app.get("/")
async def root():
    """Endpoint raíz para verificar que el servidor está funcionando."""
    return {"message": "Jarvis Server is running", "status": "online"}

# Aquí se importarán y registrarán los routers de los diferentes módulos

if __name__ == "__main__":
    # Iniciar el servidor con la configuración especificada
    uvicorn.run(
        "main:app",
        host=config["server"]["host"],
        port=config["server"]["port"],
        reload=config["server"]["debug"]
    )
