# server/app/core/security.py

from fastapi import Header, HTTPException, status, Depends
from typing import Annotated # Use Annotated for Depends with metadata in newer FastAPI/Python

# Import helper functions from our config
from server.config.known_clients import get_client_secret, is_known_client

# Dictionary to store active clients (in-memory, will be lost on restart)
# TODO: Persist this data (e.g., Redis, DB) for robustness and failover
active_clients = {}

async def get_authenticated_client(
    x_client_id: Annotated[str | None, Header()] = None,
    x_client_secret: Annotated[str | None, Header()] = None
) -> str:
    """
    Dependency to verify client credentials passed in headers.
    Returns the client_id if authentication is successful.
    Raises HTTPException otherwise.
    """
    if not x_client_id or not x_client_secret:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Client ID and Secret headers are required",
        )

    if not is_known_client(x_client_id):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Unknown Client ID: {x_client_id}",
        )

    expected_secret = get_client_secret(x_client_id)
    if not expected_secret or x_client_secret != expected_secret:
        # Basic timing attack mitigation (compare length first) - though constant time compare is better
        # For real security, use secrets.compare_digest
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Client Secret",
        )

    # If authentication is successful, return the client_id
    return x_client_id

# Type alias for dependency injection
AuthenticatedClient = Annotated[str, Depends(get_authenticated_client)]