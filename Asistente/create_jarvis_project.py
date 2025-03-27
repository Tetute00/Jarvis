#!/usr/bin/env python3
"""
Script para crear la estructura completa de directorios y archivos del proyecto JARVIS
Fecha: 2025-03-19 17:13:11
Usuario: Tetute00
"""

import os
import sys
from pathlib import Path

def create_directory(path):
    """Crea un directorio si no existe"""
    Path(path).mkdir(parents=True, exist_ok=True)
    print(f"✓ Creado directorio: {path}")

def create_file(path, content=""):
    """Crea un archivo vacío o con contenido mínimo"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Creado archivo: {path}")

def create_jarvis_structure(base_dir="jarvis"):
    """Crea la estructura completa del proyecto JARVIS"""
    print(f"\nCreando estructura del proyecto JARVIS en: {base_dir}\n")
    
    # 1. Crear directorios principales
    
    # Directorio raíz
    create_directory(base_dir)
    
    # Backend (servidor central)
    backend_dirs = [
        f"{base_dir}/backend",
        f"{base_dir}/backend/api",
        f"{base_dir}/backend/services",
        f"{base_dir}/backend/models",
        f"{base_dir}/backend/utils",
        f"{base_dir}/backend/db",
        f"{base_dir}/backend/db/migrations",
        f"{base_dir}/backend/db/seeds",
        f"{base_dir}/backend/websockets",
        f"{base_dir}/backend/tests"
    ]
    
    # Frontend (interfaz web)
    frontend_dirs = [
        f"{base_dir}/frontend",
        f"{base_dir}/frontend/css",
        f"{base_dir}/frontend/css/components",
        f"{base_dir}/frontend/css/themes",
        f"{base_dir}/frontend/js",
        f"{base_dir}/frontend/js/utils",
        f"{base_dir}/frontend/js/components",
        f"{base_dir}/frontend/js/views",
        f"{base_dir}/frontend/img",
        f"{base_dir}/frontend/img/icons",
        f"{base_dir}/frontend/img/backgrounds",
        f"{base_dir}/frontend/public",
        f"{base_dir}/frontend/public/fonts"
    ]
    
    # Clientes específicos por SO
    clients_dirs = [
        f"{base_dir}/clients",
        f"{base_dir}/clients/windows_client",
        f"{base_dir}/clients/windows_client/modules",
        f"{base_dir}/clients/windows_client/tests",
        f"{base_dir}/clients/kali_client",
        f"{base_dir}/clients/kali_client/modules",
        f"{base_dir}/clients/kali_client/tests"
    ]
    
    # Hardware (ESP32-S3)
    hardware_dirs = [
        f"{base_dir}/hardware",
        f"{base_dir}/hardware/jarvis_controller",
        f"{base_dir}/hardware/libraries",
        f"{base_dir}/hardware/schematics"
    ]
    
    # Documentación
    docs_dirs = [
        f"{base_dir}/docs",
        f"{base_dir}/docs/diagrams",
        f"{base_dir}/docs/screenshots"
    ]
    
    # Crear todos los directorios
    all_dirs = backend_dirs + frontend_dirs + clients_dirs + hardware_dirs + docs_dirs
    for dir_path in all_dirs:
        create_directory(dir_path)
    
    # 2. Crear archivos principales
    
    # Archivos raíz
    root_files = [
        (f"{base_dir}/README.md", "# JARVIS\n\nJust A Rather Very Intelligent System\n\nAsistente personal digital avanzado"),
        (f"{base_dir}/.gitignore", "# Python\n__pycache__/\n*.py[cod]\n\n# Entorno virtual\nvenv/\n.env\n\n# Logs\n*.log\n\n# Dependencias\nnode_modules/"),
        (f"{base_dir}/docker-compose.yml", "version: '3.8'\n\nservices:\n  # Servicios Docker aquí"),
        (f"{base_dir}/.env.example", "# Variables de entorno\nSERVER_PORT=5000\nGEMINI_API_KEY=your_key_here")
    ]
    
    # Backend
    backend_files = [
        (f"{base_dir}/backend/app.py", "# Aplicación principal Flask"),
        (f"{base_dir}/backend/config.py", "# Configuración del backend"),
        (f"{base_dir}/backend/requirements.txt", "flask\nflask-socketio\npython-dotenv\nrequests"),
        (f"{base_dir}/backend/Dockerfile", "FROM python:3.12-slim\n\nWORKDIR /app"),
        # API
        (f"{base_dir}/backend/api/__init__.py", ""),
        (f"{base_dir}/backend/api/system_routes.py", "# Rutas para control del sistema"),
        (f"{base_dir}/backend/api/monitor_routes.py", "# Rutas para monitorización"),
        (f"{base_dir}/backend/api/ai_routes.py", "# Rutas para IA (Gemini)"),
        (f"{base_dir}/backend/api/settings_routes.py", "# Rutas para configuración"),
        # Servicios
        (f"{base_dir}/backend/services/__init__.py", ""),
        (f"{base_dir}/backend/services/wol_service.py", "# Servicio Wake-on-LAN"),
        (f"{base_dir}/backend/services/system_service.py", "# Control del sistema"),
        (f"{base_dir}/backend/services/monitor_service.py", "# Monitorización"),
        (f"{base_dir}/backend/services/ai_service.py", "# Integración con Gemini"),
        (f"{base_dir}/backend/services/esp32_service.py", "# Comunicación con ESP32"),
        # Modelos
        (f"{base_dir}/backend/models/__init__.py", ""),
        (f"{base_dir}/backend/models/system_status.py", "# Modelo de estado del sistema"),
        (f"{base_dir}/backend/models/device.py", "# Modelo de dispositivo"),
        # Utils
        (f"{base_dir}/backend/utils/__init__.py", ""),
        (f"{base_dir}/backend/utils/network_utils.py", "# Utilidades de red"),
        # DB
        (f"{base_dir}/backend/db/__init__.py", ""),
        (f"{base_dir}/backend/db/database.py", "# Configuración de BD"),
        # Websockets
        (f"{base_dir}/backend/websockets/__init__.py", ""),
        (f"{base_dir}/backend/websockets/manager.py", "# Gestor de WebSockets")
    ]
    
    # Frontend
    frontend_files = [
        (f"{base_dir}/frontend/index.html", "<!DOCTYPE html>\n<html>\n<head>\n  <title>JARVIS</title>\n</head>\n<body>\n  <h1>JARVIS</h1>\n</body>\n</html>"),
        (f"{base_dir}/frontend/manifest.json", "{\n  \"name\": \"JARVIS\",\n  \"short_name\": \"JARVIS\"\n}"),
        (f"{base_dir}/frontend/service-worker.js", "// Service Worker para PWA"),
        (f"{base_dir}/frontend/css/main.css", "/* Estilos principales */"),
        (f"{base_dir}/frontend/js/app.js", "// Aplicación principal"),
        (f"{base_dir}/frontend/js/api.js", "// Cliente API"),
        (f"{base_dir}/frontend/js/websocket.js", "// Cliente WebSocket")
    ]
    
    # Clients
    clients_files = [
        # Windows
        (f"{base_dir}/clients/windows_client/jarvis_agent.py", "# Agente JARVIS para Windows"),
        (f"{base_dir}/clients/windows_client/install.bat", "@echo off\necho Instalando JARVIS Windows Agent..."),
        (f"{base_dir}/clients/windows_client/requirements.txt", "requests\npsutil\nwatchdog"),
        (f"{base_dir}/clients/windows_client/config.yml", "# Configuración del cliente Windows"),
        # Kali
        (f"{base_dir}/clients/kali_client/jarvis_agent.py", "# Agente JARVIS para Kali Linux"),
        (f"{base_dir}/clients/kali_client/install.sh", "#!/bin/bash\necho 'Instalando JARVIS Kali Agent...'"),
        (f"{base_dir}/clients/kali_client/requirements.txt", "requests\npsutil\nwatchdog"),
        (f"{base_dir}/clients/kali_client/config.yml", "# Configuración del cliente Kali"),
        (f"{base_dir}/clients/kali_client/jarvis.service", "[Unit]\nDescription=JARVIS Kali Agent")
    ]
    
    # Hardware
    hardware_files = [
        (f"{base_dir}/hardware/jarvis_controller/jarvis_controller.ino", "// Código principal para ESP32-S3"),
        (f"{base_dir}/hardware/jarvis_controller/config.h", "// Configuración del controlador"),
        (f"{base_dir}/hardware/jarvis_controller/keyboard_control.h", "// Control de teclado"),
        (f"{base_dir}/hardware/jarvis_controller/boot_detector.h", "// Detector de arranque GRUB"),
        (f"{base_dir}/hardware/schematics/README.md", "# Esquemas de conexión para el hardware")
    ]
    
    # Docs
    docs_files = [
        (f"{base_dir}/docs/architecture.md", "# Arquitectura de JARVIS"),
        (f"{base_dir}/docs/api_spec.md", "# Especificación de API"),
        (f"{base_dir}/docs/installation.md", "# Guía de instalación de JARVIS")
    ]
    
    # Crear todos los archivos
    all_files = root_files + backend_files + frontend_files + clients_files + hardware_files + docs_files
    for file_path, content in all_files:
        create_file(file_path, content)
    
    print("\n✅ Estructura de archivos de JARVIS creada exitosamente")
    print(f"El proyecto se ha inicializado en: {os.path.abspath(base_dir)}")
    print("\nSiguientes pasos según la planificación:")
    print("1. Configurar el entorno de desarrollo")
    print("2. Implementar el servidor Flask básico")
    print("3. Configurar Docker para desarrollo")

if __name__ == "__main__":
    # Usar el directorio proporcionado como argumento o el predeterminado
    directory = sys.argv[1] if len(sys.argv) > 1 else "jarvis"
    create_jarvis_structure(directory)