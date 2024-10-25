# Use an official Python runtime as a base image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the FastAPI app code
COPY . .

# Expose port 8080 and run the FastAPI app
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]