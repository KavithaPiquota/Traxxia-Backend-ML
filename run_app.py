#!/usr/bin/env python3
"""
Simple script to run the Traxxia Backend ML Application
Alternative to Docker when Docker is not available
"""

import os
import sys
import subprocess
from pathlib import Path

def check_env_file():
    """Check if .env file exists and has required keys"""
    env_file = Path(".env")
    if not env_file.exists():
        print("❌ .env file not found!")
        print("📝 Please create a .env file with your API keys:")
        print("   cp .env.example .env")
        print("   Then edit .env and add your actual API keys:")
        print("   - NEWSAPI_API_KEY=your_actual_newsapi_key")
        print("   - OPENAI_API_KEY=sk-your_actual_openai_key")
        print("")
        print("🔗 Get your API keys from:")
        print("   - NewsAPI: https://newsapi.org/")
        print("   - OpenAI: https://platform.openai.com/api-keys")
        return False
    
    # Check if keys are present (basic check)
    with open(".env", "r") as f:
        content = f.read()
        if "NEWSAPI_API_KEY=" not in content or "OPENAI_API_KEY=" not in content:
            print("⚠️  .env file exists but may be missing required keys")
            print("   Make sure it contains:")
            print("   - NEWSAPI_API_KEY=your_actual_newsapi_key")
            print("   - OPENAI_API_KEY=sk-your_actual_openai_key")
    
    return True

def install_requirements():
    """Install Python requirements"""
    print("📦 Installing Python dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False

def run_app():
    """Run the FastAPI application"""
    if not check_env_file():
        return False
    
    print("🚀 Setting up Traxxia Backend ML Application...")
    
    # Install requirements
    if not install_requirements():
        return False
    
    # Run the application
    print("🎯 Starting FastAPI application on port 8000...")
    print("📡 API will be available at: http://localhost:8000")
    print("📚 API documentation at: http://localhost:8000/docs")
    print("")
    print("Press Ctrl+C to stop the server")
    print("")
    
    try:
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "openai_analyzer:app", 
            "--host", "0.0.0.0", 
            "--port", "8000", 
            "--reload"
        ])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error running application: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = run_app()
    sys.exit(0 if success else 1)
