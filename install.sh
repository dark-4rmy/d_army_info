#!/bin/bash

# d-army informations getting IP or URL - Installation Script

# Check if Python is installed
if command -v python3 &>/dev/null; then
    echo "Python is installed."
else
    echo "Python is not installed. Please install Python 3."
    exit 1
fi

# Check if pip is installed
if command -v pip &>/dev/null; then
    echo "pip is installed."
else
    echo "pip is not installed. Please install pip."
    exit 1
fi

# Install required libraries
echo "Installing required libraries..."
pip install whois networkx matplotlib --break-system-packages

echo "Installation complete!"
echo "You can now run the tool using: python3 d_army_info.py"
