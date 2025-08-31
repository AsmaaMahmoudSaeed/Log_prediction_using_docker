FROM python:3.11.13

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and model
COPY src/ ./src/
COPY models/ ./models/

# Expose the dynamic port provided by Render
EXPOSE $PORT

# Run the Streamlit app with Gunicorn and Uvicorn workers
CMD ["gunicorn", "--worker-class=uvicorn.workers.UvicornWorker", "--workers=2", "--bind=0.0.0.0:$PORT", "--timeout=120", "src.main:main"]