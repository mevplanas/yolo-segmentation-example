# YOLO framework 
from ultralytics import YOLO

# OS traversal 
import os 

# YAML reading 
import yaml

# Drawing the masks 
from PIL import ImageDraw, Image

# If the file is run, run the bellow logic 
if __name__ == '__main__': 
    # Infering the current dir 
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Loading the configuration.yaml file 
    with open(os.path.join(current_dir, 'configuration.yaml'), 'r') as f:
        config = yaml.safe_load(f)

    # Infering which model to use 
    model_to_use = config['model_to_use']

    # Defining the full path to model 
    model_path = os.path.join(current_dir, model_to_use)

    # Loading the model 
    model = YOLO(model_path)

    # Reading all the images in the validation_iamges dir 
    path_to_images = os.path.join(current_dir, 'validation_images')
    images = os.listdir(path_to_images)

    # Creating the output directory 
    output_dir = os.path.join(current_dir, 'validation_images_output')
    os.makedirs(output_dir, exist_ok=True)

    # Iterating over the images 
    for image in images:
        # Defining the full path to image 
        image_path = os.path.join(path_to_images, image)

        # Reading the image 
        img = Image.open(image_path)

        # Saving the original shape 
        w, h = img.size

        # Predicting the image 
        results = model(img, imgsz=(w, h))

        # Drawing all the masks on the images
        draw = ImageDraw.Draw(img)
        
        for r in results:
            # Getting the polygons 
            polygons = r.masks.segments

            # Iterating over the polygons
            for polygon in polygons:

                # Converting normalized coordinates to absolute coordinates
                polygon = [(x * w, y * h) for x, y in polygon]

                # Drawing the polygon 
                draw.polygon(polygon, outline='red', width=6)

        # Saving the image to the output 
        img.save(os.path.join(output_dir, image))
