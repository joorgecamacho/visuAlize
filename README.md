sssss# VisuAlize - Blind Assistance App

VisuAlize is an application designed to assist blind people by recognizing their environment using Apple's FastVLM model. It consists of a FastAPI backend and a React frontend.

## 📚 Documentation

- [System Architecture](docs/ARCHITECTURE.md)
- [Backend & API](docs/BACKEND.md)
- [Frontend Details](docs/FRONTEND.md)

## Prerequisites

Before you begin, ensure you have the following installed:
- [Docker](https://www.docker.com/get-started) & [Docker Compose](https://docs.docker.com/compose/install/) (Recommended)
- [Python 3.8+](https://www.python.org/downloads/) (For manual backend setup)
- [Node.js 18+](https://nodejs.org/) (For manual frontend setup)
- NVIDIA GPU with drivers installed (Recommended for model performance)

---

## 🚀 Quick Start (Docker)

The easiest way to run the project is using Docker Compose.

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository-url>
    cd VisuAlize
    ```

2.  **Run the application**:
    ```bash
    docker-compose up --build
    ```

    This will start:
    - **Backend**: http://localhost:8000
    - **Frontend**: http://localhost:5173

    *Note: The first run might take a while as it downloads the necessary Docker images and model weights.*

---

## 🛠 Manual Installation

If you prefer to run the services locally without Docker, follow these steps.

### 1. Backend Setup

1.  Navigate to the backend directory:
    ```bash
    cd backend
    ```

2.  Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```

3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4.  Run the server:
    ```bash
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ```
    The backend will be available at `http://localhost:8000`.

### 2. Frontend Setup

1.  Navigate to the frontend directory:
    ```bash
    cd frontend
    ```

2.  Install dependencies:
    ```bash
    npm install
    ```

3.  Run the development server:
    ```bash
    npm run dev
    ```
    The frontend will be available at `http://localhost:5173`.

---

## 📡 API Endpoints

- **`GET /`**: Health check. Returns `{"message": "VisuAlize Backend is running"}`.
- **`POST /analyze`**: Upload an image to get a description.
    - Body: `multipart/form-data` with `file` field.

## ⚠️ Troubleshooting

- **GPU Issues**: If you encounter issues with GPU detection in Docker, ensure you have the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) installed.
- **Model Loading**: The model downloads automatically on the first run. Ensure you have a stable internet connection.
