from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n-seg.pt')  # load a pretrained model (recommended for training)

# Train the model
model.train(data='configuration.yaml', epochs=10, imgsz=640)