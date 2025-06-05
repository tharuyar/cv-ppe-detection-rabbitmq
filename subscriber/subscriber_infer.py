# 📁 subscriber/subscriber.py
# Description: RabbitMQ subscriber using YOLOv5 (detects PPE violations from video frames)

import base64
import json
import pika
import cv2
import torch
import numpy as np
import os
import time

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path=r"C:\Users\Tharun\OneDrive\Documents\cv_ppe_detection_rabbitmq\detection_model\best.pt",force_reload=True)

# RabbitMQ setup
QUEUE_NAME = 'frame_queue'
RABBITMQ_HOST = 'localhost'
# Connect to RabbitMQ

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RABBITMQ_HOST))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)


def callback(ch, method, properties, body):
    message = json.loads(body)
    frame_data = base64.b64decode(message["image"])
    np_arr = np.frombuffer(frame_data, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # Inference with YOLOv5
    results = model(frame)
    detections = results.pandas().xyxy[0]  # Get predictions as DataFrame

    print(f"[Subscriber] Inference Results:")
    print(detections[['name', 'confidence']])

    # Draw boxes
    for _, row in detections.iterrows():
        label = row['name']
        conf = row['confidence']
        x1, y1, x2, y2 = map(
            int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Display frame
    cv2.imshow("PPE Detection - YOLOv5", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        channel.stop_consuming()


# Consume frames
channel.basic_consume(
    queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)
print('[Subscriber] Waiting for frames...')
channel.start_consuming()
