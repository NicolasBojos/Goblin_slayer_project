from ultralytics import YOLO
from tracking import delayed_bot_and_tracking

# **Load YOLO Model (Make sure best.pt exists)**
model = YOLO(r"C:/Users/nicol/Computer Vision Group/best.pt")

# **Run Bot**
delayed_bot_and_tracking(model)
