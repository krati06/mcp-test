
FROM python:3.9-slim

WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the port
EXPOSE 8080

# Command to run the application
CMD ["uvicorn", "mcp_server:app", "--host", "0.0.0.0", "--port", "8080"]
