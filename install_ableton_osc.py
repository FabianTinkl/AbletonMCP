#!/usr/bin/env python3
"""
AbletonOSC Installation Helper Script
"""

import os
import platform
import subprocess
import sys
from pathlib import Path
import urllib.request
import zipfile
import shutil

def get_ableton_remote_scripts_path():
    """Get the path to Ableton Live's Remote Scripts directory."""
    system = platform.system()
    
    if system == "Darwin":  # macOS
        # Check common Ableton Live installation paths
        possible_paths = [
            Path.home() / "Library" / "Application Support" / "Ableton" / "Live 11" / "Preferences" / "User Remote Scripts",
            Path.home() / "Library" / "Application Support" / "Ableton" / "Live 12" / "Preferences" / "User Remote Scripts",
            Path.home() / "Music" / "Ableton" / "User Library" / "Remote Scripts"
        ]
    elif system == "Windows":
        # Windows paths
        possible_paths = [
            Path.home() / "Documents" / "Ableton" / "User Library" / "Remote Scripts",
            Path(os.environ.get("USERPROFILE", "")) / "Documents" / "Ableton" / "User Library" / "Remote Scripts"
        ]
    else:  # Linux
        possible_paths = [
            Path.home() / ".ableton" / "Live" / "User Library" / "Remote Scripts"
        ]
    
    # Find the first existing path
    for path in possible_paths:
        if path.exists():
            return path
    
    # If none exist, return the most likely path for creation
    return possible_paths[0] if possible_paths else None

def download_ableton_osc():
    """Download AbletonOSC from GitHub."""
    print("📥 Downloading AbletonOSC...")
    
    url = "https://github.com/ideoforms/AbletonOSC/archive/refs/heads/main.zip"
    temp_file = Path("AbletonOSC-main.zip")
    
    try:
        urllib.request.urlretrieve(url, temp_file)
        print("✅ Download completed")
        return temp_file
    except Exception as e:
        print(f"❌ Download failed: {e}")
        return None

def install_ableton_osc():
    """Install AbletonOSC to Ableton Live's Remote Scripts directory."""
    print("🎵 Installing AbletonOSC for Ableton Live...")
    
    # Get Remote Scripts path
    remote_scripts_path = get_ableton_remote_scripts_path()
    if not remote_scripts_path:
        print("❌ Could not find Ableton Live Remote Scripts directory")
        print("Please manually create the directory and run this script again:")
        if platform.system() == "Darwin":
            print("  ~/Music/Ableton/User Library/Remote Scripts")
        else:
            print("  ~/Documents/Ableton/User Library/Remote Scripts")
        return False
    
    print(f"📂 Using Remote Scripts path: {remote_scripts_path}")
    
    # Create directory if it doesn't exist
    remote_scripts_path.mkdir(parents=True, exist_ok=True)
    
    # Download AbletonOSC
    zip_file = download_ableton_osc()
    if not zip_file:
        return False
    
    try:
        # Extract the zip file
        print("📦 Extracting AbletonOSC...")
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(".")
        
        # Move the AbletonOSC folder to Remote Scripts
        source_path = Path("AbletonOSC-main")
        target_path = remote_scripts_path / "AbletonOSC"
        
        if target_path.exists():
            print("🔄 Removing existing AbletonOSC installation...")
            shutil.rmtree(target_path)
        
        shutil.move(str(source_path), str(target_path))
        
        # Clean up
        zip_file.unlink()
        
        print("✅ AbletonOSC installed successfully!")
        print(f"📁 Installed to: {target_path}")
        
        return True
        
    except Exception as e:
        print(f"❌ Installation failed: {e}")
        return False

def print_configuration_instructions():
    """Print instructions for configuring AbletonOSC in Ableton Live."""
    print("""
🔧 **Configuration Instructions:**

1. Open Ableton Live
2. Go to Preferences (Live → Preferences on macOS, Options → Preferences on Windows)
3. Select the "Link/Tempo/MIDI" tab
4. In the Control Surface section:
   - Set the first dropdown to "AbletonOSC"
   - Leave Input and Output set to "None"
5. Click "OK" to save

🎵 **Testing the Connection:**

1. Restart Ableton Live
2. Run the MCP server: `python -m mcp_server.main`
3. The server should connect automatically to Live

📋 **Troubleshooting:**

• If AbletonOSC doesn't appear in the Control Surface dropdown:
  - Make sure Ableton Live is completely closed before installation
  - Check the Remote Scripts path is correct
  - Restart Ableton Live

• If connection fails:
  - Check that AbletonOSC is selected in Live's preferences
  - Verify Live is running when starting the MCP server
  - Check the console for error messages

🔗 **Default Ports:**
• To Live: 11000
• From Live: 11001

For more information: https://github.com/ideoforms/AbletonOSC
""")

def main():
    """Main installation process."""
    print("🎵 AbletonOSC Installation Helper")
    print("=" * 40)
    
    if len(sys.argv) > 1 and sys.argv[1] == "--instructions-only":
        print_configuration_instructions()
        return
    
    print("This script will download and install AbletonOSC for Ableton Live.")
    print("AbletonOSC enables OSC communication between Ableton Live and external applications.")
    print("")
    
    response = input("Continue with installation? (y/N): ").lower().strip()
    if response != 'y':
        print("Installation cancelled.")
        return
    
    # Install AbletonOSC
    success = install_ableton_osc()
    
    if success:
        print("")
        print("🎉 Installation completed successfully!")
        print_configuration_instructions()
    else:
        print("")
        print("❌ Installation failed. Please install manually:")
        print("1. Download: https://github.com/ideoforms/AbletonOSC")
        print("2. Extract to your Ableton Live Remote Scripts directory")
        print("3. Restart Ableton Live and configure as shown above")

if __name__ == "__main__":
    main()