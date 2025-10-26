#!/bin/bash

# Traxxia Backend ML Application Setup and Run Script

echo "🚀 Setting up Traxxia Backend ML Application..."

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "❌ .env file not found!"
    echo "📝 Please create a .env file with your API keys:"
    echo "   cp .env.example .env"
    echo "   Then edit .env and add your actual API keys:"
    echo "   - NEWSAPI_API_KEY=your_actual_newsapi_key"
    echo "   - OPENAI_API_KEY=sk-your_actual_openai_key"
    echo ""
    echo "🔗 Get your API keys from:"
    echo "   - NewsAPI: https://newsapi.org/"
    echo "   - OpenAI: https://platform.openai.com/api-keys"
    exit 1
fi

# Check if virtual environment exists, create if not
if [ ! -d "venv" ]; then
    echo "🐍 Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Run the application
echo "🎯 Starting FastAPI application on port 8000..."
echo "📡 API will be available at: http://localhost:8000"
echo "📚 API documentation at: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

uvicorn openai_analyzer:app --host 0.0.0.0 --port 8000 --reload
