import os
import stat # Needed for making scripts executable

# --- Configuration ---
PROJECT_NAME = "JarvisProject"
DIRECTORIES = {
    "server": {
        "app": ["api", "core", "services", "models"],
        "tests": [],
        "config": [],
        "scripts": [],
    },
    "clients": {
        "windows": ["modules", "config"],
        "kali": ["modules", "config"],
        "common": [], # For shared client code
    },
    "hardware": {
        "esp32_color_sensor": ["src", "lib", "data"],
    },
    "ml": {
        "voice_recognition": ["models", "scripts"],
        "facial_recognition": ["models", "scripts", "data"], # Data for face profiles
    },
    "web_ui": {
        "frontend": ["src", "public", "components"], # Basic frontend structure
        # Assuming FastAPI serves the UI API endpoints
    },
    "docs": [],
    "tests": [], # Top-level tests (e.g., end-to-end)
    "scripts": [], # Top-level utility scripts
}

# Files to create in specific directories (path relative to root: content)
# Use None for empty files
FILES = {
    # Root
    "README.md": f"# {PROJECT_NAME}\n\nDescripción general del proyecto Jarvis.",
    ".gitignore": """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environment
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE / Editor specific
.idea/
.vscode/
*.swp
*~
*.sublime-project
*.sublime-workspace

# OS specific
.DS_Store
Thumbs.db

# Data files (Facial recognition, etc.) - Be careful committing sensitive data
ml/facial_recognition/data/
server/config/*.json # Example if you store sensitive config here
server/config/*.env

# Compiled files
*.compiled

# Logs
logs/
*.log
""",
    "requirements.txt": "# Requerimientos generales del proyecto (e.g., dev tools)\n",
    "setup_project.py": "# This script (already exists)", # Placeholder

    # Server
    "server/requirements.txt": "fastapi\nuvicorn[standard]\npython-dotenv\n# Add other server dependencies here\n",
    "server/app/main.py": """
from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables (optional, if using .env)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', 'config', '.env'))

app = FastAPI(title="Jarvis Server")

@app.get("/")
async def read_root():
    return {"message": "Jarvis Server is running"}

# Placeholder for future API routers
# from .api import auth, commands # Example
# app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
# app.include_router(commands.router, prefix="/commands", tags=["Commands"])

if __name__ == "__main__":
    port = int(os.getenv("SERVER_PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
""",
    "server/app/__init__.py": None,
    "server/app/api/__init__.py": None,
    "server/app/core/__init__.py": None,
    "server/app/services/__init__.py": None,
    "server/app/models/__init__.py": None,
    "server/config/.env_example": "SERVER_PORT=8000\nSECRET_KEY=generate_a_strong_secret_key\n# Add other config variables",
    "server/tests/__init__.py": None,
    "server/scripts/run_server.sh": """
#!/bin/bash
# Script to run the FastAPI server

# Navigate to the server directory (adjust path if needed)
cd "$(dirname "$0")/../" || exit

# Activate virtual environment if you use one
# source ../.venv/bin/activate

echo "Starting Jarvis Server..."
# Use uvicorn directly or python main.py depending on your preference
# uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
python app/main.py
""",


    # Clients
    "clients/windows/client_app.py": "# Main script for Windows client\nimport time\n\nprint('Jarvis Windows Client starting...')\n# Add connection logic here\nwhile True:\n    time.sleep(10)\n",
    "clients/windows/requirements.txt": "requests\n# Add other windows client dependencies\n",
    "clients/windows/modules/__init__.py": None,
    "clients/windows/config/.env_example": "SERVER_URL=http://<chromebook_ip>:8000\nCLIENT_ID=windows_pc_1\nCLIENT_SECRET=generate_secret\n",

    "clients/kali/client_app.py": "# Main script for Kali Linux client\nimport time\n\nprint('Jarvis Kali Client starting...')\n# Add connection logic here\nwhile True:\n    time.sleep(10)\n",
    "clients/kali/requirements.txt": "requests\n# Add other kali client dependencies\n",
    "clients/kali/modules/__init__.py": None,
    "clients/kali/config/.env_example": "SERVER_URL=http://<chromebook_ip>:8000\nCLIENT_ID=kali_pc_1\nCLIENT_SECRET=generate_secret\n",

    "clients/common/__init__.py": None,

    # Hardware
    "hardware/esp32_color_sensor/src/esp32_color_sensor.ino": "// Arduino code for ESP32 color sensor\n\nvoid setup() {\n  Serial.begin(115200);\n  Serial.println(\"ESP32 Color Sensor Initializing...\");\n  // Add sensor initialization code here\n}\n\nvoid loop() {\n  // Add color reading and communication logic here\n  delay(1000);\n}\n",
    "hardware/esp32_color_sensor/README.md": "# ESP32 Color Sensor\n\nCode and documentation for the ESP32 component.",

    # ML
    "ml/voice_recognition/__init__.py": None,
    "ml/facial_recognition/__init__.py": None,
    "ml/facial_recognition/data/.gitkeep": None, # Keep the directory, but data should be gitignored

    # Web UI
    "web_ui/frontend/src/main.js": "// Main entry point for the frontend application (e.g., Vue, React)\nconsole.log('Web UI Initializing...');",
    "web_ui/frontend/public/index.html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jarvis Control Panel</title>
</head>
<body>
    <div id="app">
        <h1>Jarvis Control Panel</h1>
        <p>Loading...</p>
    </div>
    <!-- Link to your compiled JS file -->
    <!-- <script type="module" src="/src/main.js"></script> -->
</body>
</html>
""",
    "web_ui/README.md": "# Jarvis Web Control Panel\n\nFrontend and related files for the web interface.",

    # Docs
    "docs/architecture.md": "# Arquitectura del Sistema Jarvis\n\nDocumentación detallada de la arquitectura.",
    "docs/setup.md": "# Guía de Instalación de Jarvis\n\nPasos para configurar el servidor y los clientes.",
}

# --- Script Logic ---
def create_dir(path):
    """Creates a directory if it doesn't exist."""
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Created directory: {path}")
    except OSError as e:
        print(f"Error creating directory {path}: {e}")

def create_file(path, content=None):
    """Creates a file, optionally with content, if it doesn't exist."""
    if not os.path.exists(path):
        try:
            with open(path, 'w', encoding='utf-8') as f:
                if content:
                    f.write(content.strip())
            print(f"Created file:      {path}")
            # Make shell scripts executable
            if path.endswith(".sh"):
                try:
                    # Add execute permission for owner and group u+x, g+x
                    st = os.stat(path)
                    os.chmod(path, st.st_mode | stat.S_IXUSR | stat.S_IXGRP)
                    print(f"Made executable: {path}")
                except Exception as chmod_e:
                    print(f"Warning: Could not set execute permission on {path}: {chmod_e}")

        except OSError as e:
            print(f"Error creating file {path}: {e}")
    # else: # Optional: message if file already exists
    #     print(f"File exists:     {path}")


def main():
    """Main function to create project structure."""
    project_root = PROJECT_NAME
    print(f"Creating project structure for '{project_root}'...")

    # Create root directory
    create_dir(project_root)

    # Create main directories and subdirectories
    for main_dir, sub_dirs_dict in DIRECTORIES.items():
        current_path = os.path.join(project_root, main_dir)
        create_dir(current_path)
        if isinstance(sub_dirs_dict, dict): # Handle nested dict structure
             for sub_dir, nested_sub_dirs in sub_dirs_dict.items():
                 sub_path = os.path.join(current_path, sub_dir)
                 create_dir(sub_path)
                 for nested in nested_sub_dirs:
                     nested_path = os.path.join(sub_path, nested)
                     create_dir(nested_path)
        elif isinstance(sub_dirs_dict, list): # Handle flat list structure
             for sub_dir in sub_dirs_dict:
                 sub_path = os.path.join(current_path, sub_dir)
                 create_dir(sub_path)


    # Create specified files
    for file_path_rel, content in FILES.items():
        full_path = os.path.join(project_root, file_path_rel)
        # Ensure parent directory exists before creating file
        parent_dir = os.path.dirname(full_path)
        if parent_dir:
            create_dir(parent_dir) # `create_dir` handles existing dirs
        create_file(full_path, content)

    print("\nProject structure created successfully!")
    print(f"Navigate to '{project_root}' directory to start working.")

if __name__ == "__main__":
    main()