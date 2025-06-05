# 📁 Dockerfile
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy code
COPY subscriber/ ./

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Download YOLOv5 model and code on build
RUN python -c "import torch; torch.hub.download_url_to_file('https://github.com/ultralytics/yolov5/archive/refs/heads/master.zip', 'yolov5.zip')"

# Set entry point
CMD ["python", "subscriber.py"]
# Expose port if needed (optional, uncomment if required)
# EXPOSE 5000