from ultralytics import YOLO

# Load a model
model = YOLO('yolov8l-seg.pt')  # load a pretrained model (recommended for training)

# Train the model
model.train(data='configuration.yaml', epochs=20, imgsz=900)