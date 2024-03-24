# Adjust the import statement based on the specific Ultralytics YOLO version you're using
from ultralytics import YOLO

# Load the model (ensure the path to your model weights file is correct)
model = YOLO(r"C:\Users\user\MidasMap\ai-depth-map-single-camera-with-midas\best.pt")

# Perform detection on a video source (e.g., webcam)
model.predict(source="0", show=True, conf=0.3)
