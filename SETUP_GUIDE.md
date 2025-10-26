# Traxxia Backend ML - Setup Guide

This is a FastAPI application for strategic business analysis using OpenAI and NewsAPI.

## Prerequisites

- Python 3.11+
- API Keys:
  - **NewsAPI Key**: Get from [https://newsapi.org/](https://newsapi.org/)
  - **OpenAI API Key**: Get from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

## Setup Instructions

### Step 1: Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file and add your actual API keys:
   ```
   NEWSAPI_API_KEY=your_actual_newsapi_key_here
   OPENAI_API_KEY=sk-your_actual_openai_key_here
   ```

### Step 2: Choose Your Running Method

#### Option A: Using the Setup Script (Recommended)
```bash
./setup_and_run.sh
```

#### Option B: Using Python Script
```bash
python3 run_app.py
```

#### Option C: Manual Setup
```bash
# Create virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn openai_analyzer:app --host 0.0.0.0 --port 8000 --reload
```

#### Option D: Using Docker (if Docker is installed)
```bash
# Build the Docker image
docker build -t simple-app:v1 .

# Run the container
docker run -it -p 8000:8000 simple-app:v1
```

## Accessing the Application

Once running, the application will be available at:
- **API Base URL**: http://localhost:8000
- **Interactive API Documentation**: http://localhost:8000/docs
- **Alternative API Docs**: http://localhost:8000/redoc

## API Endpoints

The application provides various strategic analysis endpoints:

- `GET /` - Health check
- `POST /analyze` - Analyze question-answer pairs
- `POST /upload-and-analyze` - Upload files and analyze
- `POST /pestel-analysis` - PESTEL analysis
- `POST /porter-analysis` - Porter's Five Forces analysis
- `POST /strategic-goals` - Strategic goals and OKR analysis
- `POST /competitive-advantage` - Competitive advantage analysis
- And many more...

## Troubleshooting

### Common Issues

1. **Missing API Keys**: Make sure your `.env` file contains valid API keys
2. **Port Already in Use**: If port 8000 is busy, change it in the run command
3. **Python Dependencies**: Ensure all requirements are installed correctly

### Getting Help

- Check the FastAPI documentation at `/docs` endpoint
- Verify your API keys are valid and have sufficient credits
- Ensure Python 3.11+ is installed

## Development

For development with auto-reload:
```bash
uvicorn openai_analyzer:app --host 0.0.0.0 --port 8000 --reload
```

## Security Notes

- Never commit your `.env` file to version control
- Keep your API keys secure and rotate them regularly
- The `.env` file is already in `.gitignore` for security
