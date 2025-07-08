# Chat Backend Multisession

This is a Python application using FastAPI for building a chat backend with multisession support.

## Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/installation/)
- (Optional) [virtualenv](https://virtualenv.pypa.io/en/latest/)

## Installation

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd chat_backend_multisession
    ```

2. **Create and activate a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. **Start the FastAPI server:**
    ```bash
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
    ```
    - Replace `main` with the name of your main Python file if different.

2. **Access the API docs:**
    - Open [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs) in your browser.

## Environment Variables

- Create a `.env` file in the project root if needed for configuration.

## Testing

- Run tests (if available):
  ```bash
  pytest
  ```

## License

See [LICENSE](LICENSE) for details.