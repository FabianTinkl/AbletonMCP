#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path

def run_command(command, check=True):
    """Run a shell command and return the result."""
    print(f"Running: {command}")
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            check=check, 
            capture_output=True, 
            text=True
        )
        if result.stdout:
            print(result.stdout)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Return code: {e.returncode}")
        print(f"Error output: {e.stderr}")
        if check:
            raise
        return e

def setup_environment():
    """Set up the development environment."""
    print("Setting up AbletonMCP development environment...")
    
    # Check if we're in a virtual environment
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("Virtual environment detected.")
    else:
        print("Warning: Not in a virtual environment. Consider using 'python -m venv venv' first.")
    
    # Install dependencies
    print("\nInstalling dependencies...")
    run_command(f"{sys.executable} -m pip install --upgrade pip")
    run_command(f"{sys.executable} -m pip install -r requirements.txt")
    
    # Install the package in development mode
    print("\nInstalling package in development mode...")
    run_command(f"{sys.executable} -m pip install -e .")
    
    print("\n✅ Setup complete!")
    print("\nNext steps:")
    print("1. Install AbletonOSC in your Ableton Live Remote Scripts folder")
    print("2. Configure Claude Desktop to use this MCP server")
    print("3. Run: python -m mcp_server.main")

if __name__ == "__main__":
    setup_environment()