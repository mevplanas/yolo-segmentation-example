from ultralytics import YOLO
# Load a model
model = YOLO('yolov8m-seg.pt') # load a pretrained model (recommended for training)

# Train the model
model.train(data='configuration.yaml', epochs=40, imgsz=1024)