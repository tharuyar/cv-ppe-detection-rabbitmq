# 📁 File: Dockerfile (for subscriber container)

FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install system dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy subscriber code
COPY subscriber/ ./subscriber/

# Run the subscriber
CMD ["python", "subscriber/subscriber_infer.py"]