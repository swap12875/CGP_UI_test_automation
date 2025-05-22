#!/bin/bash

# Update package list
sudo apt-get update

# Install Python and pip
sudo apt-get install -y python3 python3-pip python3-venv

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Install Playwright browsers with all necessary dependencies
python3 -m playwright install --with-deps
