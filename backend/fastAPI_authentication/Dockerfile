# Use official Python image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy FastAPI app files to the container
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r req_static.txt

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
