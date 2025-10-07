# Import necessary modules for file operations and logging
import os
from pathlib import Path
import logging

# Configure logging to display informational messages with timestamps
# This helps track what the script is doing during execution
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Define the main project name - this will be used in folder structure
project_name = "cnnClassifier"

# List of all files and directories that need to be created for the ML project
# This creates a standard project structure for a CNN classifier
list_of_files = [
    # GitHub Actions workflow directory for CI/CD
    ".github/workflows/.gitkeep",
    
    # Main source code directory structure
    f"src/{project_name}/__init__.py",               # Main package init file
    f"src/{project_name}/components/__init__.py",         # ML components data ingestion, training, etc.)
    f"src/{project_name}/utils/__init__.py",              # Utility functions
    f"src/{project_name}/config/__init__.py",             # Configuration package
    f"src/{project_name}/config/configuration.py",       # Main configuration file
    f"src/{project_name}/pipeline/__init__.py",           # ML pipeline scripts
    f"src/{project_name}/entity/__init__.py",             # Data entities/classes
    f"src/{project_name}/constants/__init__.py",          # Project constants
    
    # Configuration and setup files
    "config/config.yaml",          # YAML configuration file
    "dvc.yaml",                   # Data Version Control pipeline file
    "params.yaml",                # Parameters for ML experiments
    "requirements.txt",           # Python dependencies
    "setup.py",                   # Package setup file
    "research/trials.ipynb",      # Jupyter notebook for research/experiments
]

# Loop through each file path in the list to create directory structure
for filepath in list_of_files:
    # Convert string path to Path object for better path handling
    filepath = Path(filepath)
    
    # Split the path into directory and filename components
    # os.path.split() returns a tuple: (directory_path, filename)
    filedir, filename = os.path.split(filepath)
    
    # Check if there's a directory path (not just a filename)
    if filedir != "":
        # Create the directory structure if it doesn't exist
        # exist_ok=True prevents error if directory already exists
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")
    
    # Create the file if it doesn't exist OR if it exists but is empty (0 bytes)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Create an empty file by opening in write mode and immediately closing
        with open(filepath, "w") as f:
            pass  # pass means "do nothing" - just create empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        # File already exists and has content, so skip creating it
        logging.info(f"File already exists: {filepath}, skipping creation.")
