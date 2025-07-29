# FedTec Lab Chatbot 🤖

A sophisticated chatbot application built with FastAPI and LangChain, designed to provide intelligent responses using document-based knowledge retrieval.

## 🚀 Features

- **FastAPI Backend**: High-performance REST API with automatic documentation
- **LangChain Integration**: Advanced language model capabilities with document retrieval
- **ChromaDB Vector Store**: Efficient document storage and similarity search
- **Docker Support**: Easy deployment and containerization
- **CORS Enabled**: Frontend-friendly with proper cross-origin support

## 🛠️ Quick Start

### Prerequisites
- Python 3.9+
- Docker (optional)
- Conda or pip

### Installation

```bash
# Create and activate conda environment
conda create -p venv python=3.12
conda activate venv/

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

#### Option 1: Direct Python
```bash
uvicorn app:app --host 0.0.0.0 --port 7860 --reload
```
**Access**: `http://localhost:7860`

#### Option 2: Docker
```bash
# Build and run
docker build -t fedtec-lab-chatbot-app .
docker run -d -p 8000:7860 --name fedtec-lab-chatbot-container fedtec-lab-chatbot-app
```
**Access**: `http://localhost:8000`

## 📚 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/fedtec-lab/health` | GET | Health check |
| `/langChain/fedtec-lab/chatbot` | POST | Local LangChain with document retrieval |

## 📖 API Documentation

- **Swagger UI**: `http://localhost:7860/docs` (or `:8000` for Docker)
- **ReDoc**: `http://localhost:7860/redoc` (or `:8000` for Docker)
- **OpenAPI JSON**: `http://localhost:7860/openapi.json`

## 🔧 Configuration

### Environment Variables
Create a `.env` file:
```env
OPENAI_API_KEY=your_openai_key_here
TAVILY_API_KEY=your_tavily_key_here
```

### CORS Settings
- `http://localhost:5173` (Frontend development)
- `https://sf.courts.ca.gov/` (Production)

## 📦 Key Dependencies

- **FastAPI**: Web framework
- **LangChain**: LLM framework
- **ChromaDB**: Vector database
- **Uvicorn**: ASGI server
- **OpenAI**: Language model provider

## 🏗️ Project Structure

```
fedtec-lab-chatbot/
├── app.py                 # Main FastAPI application
├── langChain_chat_model.py # LangChain implementation
├── main.py                # Alternative entry point
├── requirements.txt       # Dependencies
├── Dockerfile            # Docker configuration
├── chroma/               # Vector database storage
└── venv/                 # Virtual environment
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

**Made with ❤️ for FedTec Lab**