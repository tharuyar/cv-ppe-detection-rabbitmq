import cv2
import pika
import base64
import json
import time

QUEUE_NAME = 'frame_queue'
RABBITMQ_HOST = 'localhost'

# connect to rabbitmq
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RABBITMQ_HOST))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)


# Load PPE video
cap = cv2.VideoCapture(r"C:\Users\Tharun\OneDrive\Documents\cv_ppe_detection_rabbitmq\video\vid.mp4")
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Encode frame to jpeg and then base64
    _, buffer = cv2.imencode('.jpg', frame)
    jpg_as_text = base64.b64encode(buffer).decode('utf-8')

    # package the message
    message = json.dumps({
        "image": jpg_as_text,
        "timestamp": time.time()
    })

    # publish to Rabbitmq
    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=message)
    print("[Publisher] PPE frame sent")
cap.release()
connection.close()
