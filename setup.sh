#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Run the server setup scripts
python scripts/install_server.py
python scripts/install_plugin.py
python scripts/configure_server_properties.py
python scripts/setup_server_with_preferences.py

# Make the start_server.sh script executable
chmod +x start_server.sh

# Run the web interface
python web/app.py
