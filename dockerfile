FROM python:3.11.13

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt



# Copy application code
COPY src/ ./src/

# Create models directory (will be populated by downloading cmodel.pkl)
RUN mkdir -p models

# Expose the dynamic port provided by Render
EXPOSE $PORT

# Run the Streamlit app with Gunicorn and Uvicorn workers
CMD ["gunicorn", "--worker-class=uvicorn.workers.UvicornWorker", "--workers=2", "--bind=0.0.0.0:$PORT", "--timeout=120", "src.main:main"]