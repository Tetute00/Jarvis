# server/app/main.py

from fastapi import FastAPI, HTTPException, Depends, status
import uvicorn
import os
from dotenv import load_dotenv
from datetime import datetime, timezone
from typing import Dict, Any

# Import security dependency and active clients store
from .core.security import AuthenticatedClient, active_clients

# Load environment variables (e.g., for port)
# Ensure .env is in server/config/ or specify path
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'config', '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path=dotenv_path)
else:
     # Fallback if .env doesn't exist in config, try server/ directory
     dotenv_path_alt = os.path.join(os.path.dirname(__file__), '..', '.env')
     if os.path.exists(dotenv_path_alt):
          load_dotenv(dotenv_path=dotenv_path_alt)
     # else: print a warning or rely on system env vars


app = FastAPI(
    title="Jarvis Central Server",
    description="Core server for the Jarvis personal assistant system.",
    version="0.1.0"
)

# --- Endpoints ---

@app.get("/")
async def read_root():
    """Root endpoint for health check."""
    return {"message": "Jarvis Server is running"}

@app.post("/register")
async def register_client(client_id: AuthenticatedClient):
    """
    Endpoint for clients to announce they are online.
    Requires valid X-Client-ID and X-Client-Secret headers.
    """
    now = datetime.now(timezone.utc)
    active_clients[client_id] = {
        "status": "registered",
        "last_seen": now.isoformat(),
        "registered_at": now.isoformat()
    }
    print(f"Client registered/re-registered: {client_id}")
    return {"message": f"Client '{client_id}' registered successfully"}

@app.post("/heartbeat")
async def client_heartbeat(client_id: AuthenticatedClient):
    """
    Endpoint for clients to send periodic heartbeats.
    Requires valid X-Client-ID and X-Client-Secret headers.
    """
    if client_id not in active_clients:
        # Optional: Auto-register if heartbeat received from authenticated but unknown client
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not registered. Please register first.")
        print(f"Heartbeat from known but not actively registered client: {client_id}. Registering now.")
        await register_client(client_id) # Call register function directly
        return {"message": f"Client '{client_id}' heartbeat received (auto-registered)"}


    now = datetime.now(timezone.utc)
    active_clients[client_id]["last_seen"] = now.isoformat()
    active_clients[client_id]["status"] = "online" # Or update based on payload later
    # print(f"Heartbeat received from: {client_id}") # Can be noisy
    return {"message": f"Heartbeat from '{client_id}' received"}

@app.get("/status")
async def get_system_status(
    # Optional: Protect this endpoint too, maybe only allow specific clients (like web_ui)
    # client_id: AuthenticatedClient
    ):
    """Returns the status of currently active/registered clients."""
    # TODO: Implement proper authorization (e.g., only allow web_ui or admin clients)
    return active_clients

@app.get("/protected_test")
async def protected_route_test(client_id: AuthenticatedClient):
    """A simple protected endpoint to test authentication."""
    return {"message": f"Hello authenticated client: {client_id}"}

# --- Placeholder for future API routers ---
# from .api import auth_router, command_router # Example hypothetical routers
# app.include_router(auth_router.router, prefix="/auth", tags=["Authentication"])
# app.include_router(command_router.router, prefix="/commands", tags=["Commands"])

# --- Server Startup ---
if __name__ == "__main__":
    port = int(os.getenv("SERVER_PORT", 8000))
    host = os.getenv("SERVER_HOST", "0.0.0.0") # Listen on all interfaces by default
    print(f"Starting Jarvis Server on {host}:{port}")
    # Use uvicorn programmatically or run via 'uvicorn server.app.main:app --reload'
    uvicorn.run(app, host=host, port=port)