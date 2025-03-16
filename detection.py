from ultralytics import YOLO
import numpy as np
import cv2
from PIL import Image

# **Load YOLO Model**
model = YOLO(r"C:/Users/nicol/Computer Vision Group/best.pt")

# **Goblin Class ID**
TARGET_CLASSES = {2}

def detect_goblins(frame, model):
    """Runs YOLO detection and returns detected goblins."""

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(frame_rgb)  # Convert to PIL Image
    results = model(pil_img, imgsz=320)  # Run YOLO

    if not results or not results[0].boxes or len(results[0].boxes) == 0:
        return []

    boxes = results[0].boxes.xyxy.cpu().numpy()
    classes = results[0].boxes.cls.cpu().numpy()
    confidences = results[0].boxes.conf.cpu().numpy()

    goblins = []
    for i, box in enumerate(boxes):
        if classes[i] in TARGET_CLASSES and confidences[i] > 0.2:
            goblins.append((box, confidences[i]))

    return goblins


