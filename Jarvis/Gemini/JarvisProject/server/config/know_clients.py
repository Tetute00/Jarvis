# server/config/known_clients.py

# WARNING: Storing secrets directly like this is insecure.
# This is for initial development ONLY.
# TODO: Replace with a secure method (e.g., hashed secrets in DB/config file, Vault)
CLIENTS = {
    "windows_pc_1": {
        "secret": "SUPER_SECRET_WINDOWS_KEY", # Replace with a real random secret
        "description": "Main Windows 11 PC"
    },
    "kali_pc_1": {
        "secret": "VERY_SECRET_KALI_KEY",     # Replace with a real random secret
        "description": "Kali Linux Machine"
    },
    # Add more clients as needed
    "web_ui_internal": { # Example for potential backend communication from Web UI
        "secret": "WEB_UI_SECRET_KEY",
        "description": "Internal access for Web UI"
    }
}

def get_client_secret(client_id: str) -> str | None:
    """Retrieves the secret for a given client ID."""
    client = CLIENTS.get(client_id)
    return client.get("secret") if client else None

def is_known_client(client_id: str) -> bool:
    """Checks if a client ID is known."""
    return client_id in CLIENTS