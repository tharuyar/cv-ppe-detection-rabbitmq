## Real-Time PPE Detection System with YOLOv5, RabbitMQ, and Docker

# Overview
This project presents a real-time Personal Protective Equipment (PPE) detection system designed to enhance safety compliance on construction sites.

By leveraging YOLOv5 for object detection, RabbitMQ for message brokering, and Docker for containerization, the system efficiently processes video streams to identify safety gear such as helmets, vests, and gloves.

![image](https://github.com/user-attachments/assets/53cb88e8-34f6-42ef-b48b-1038f3aca0ed)

![vlcsnap-2025-06-05-13h50m27s902](https://github.com/user-attachments/assets/605775ac-2ff2-4dd1-87a6-b90fc0e55eec)


![image](https://github.com/user-attachments/assets/58d6e0e4-7f91-4777-a458-fffcc213c3fe)




# Objectives

-Real-Time Detection: Identify PPE compliance in live video feeds.

-Modular Architecture: Utilize a publisher-subscriber model for scalability and maintainability.

-Containerization: Deploy the system seamlessly across various environments using Docker.

-Extensibility: Lay the groundwork for future enhancements like alert systems and multi-camera support.






# Technology Stack

Programming Language: Python 3.10

Object Detection: YOLOv5

Message Broker: RabbitMQ

Containerization: Docker

Libraries:

opencv-python

pika

numpy

ultralytics








# Project Structure

cv-ppe-detection-rabbitmq/
├── publisher/              # Publishes video frames to RabbitMQ

│   └── publisher.py

├── subscriber/             # Subscribes to frames and performs detection

│   └── subscriber.py

├── detection_model/        # YOLOv5 weights (best.pt)

├── video/                  # Input video files

│   └── vid.mp4

├── Dockerfile              # Dockerfile for subscriber service

├── docker-compose.yml      # Docker Compose configuration

├── requirements.txt        # Python dependencies

└── README.md               # Project documentation




# Getting Started

# Clone the Repository

git clone https://github.com/tharuyar/cv-ppe-detection-rabbitmq.git
cd cv-ppe-detection-rabbitmq




# Set Up the Environment

Ensure you have Docker and Docker Compose installed. Then, start the services:

docker-compose up -d


This command will:

# Launch the RabbitMQ server with a management UI accessible at http://localhost:15672.

Build and run the subscriber service container.

RabbitMQ Credentials:

Username: guest

Password: guest



Run the Publisher
In a new terminal window:



# cd publisher
python publisher.py


#This script reads video frames from the specified video file and publishes them to the RabbitMQ queue.


 # Sample Output

 [Publisher] PPE frame sent
[Subscriber] Detected: ['person', 'helmet', 'vest']





# Future Enhancements
Alert System: Integrate email or SMS notifications for non-compliance detections.

Web Interface: Develop a dashboard for real-time monitoring and analytics.

Multi-Camera Support: Extend the system to handle multiple video feeds simultaneously.

Advanced Models: Explore the integration of YOLOv7 or YOLOv8 for improved accuracy.




# Author
Tharun Yara

GitHub: @tharuyar

LinkedIn: Tharun Yara
