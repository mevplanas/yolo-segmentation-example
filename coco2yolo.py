# OS traversal 
import os

# JSON reader 
import json 

# Regex 
import re 

if __name__ == '__main__': 
    # Infering the current working directory 
    current_dir = os.getcwd()

    # Defining the path to the coco dataset
    path_to_coco = os.path.join(current_dir, 'coco_format')

    # Loading all the images 
    files = os.listdir(os.path.join(path_to_coco))

    # Creating the output directory 
    output_dir = os.path.join(current_dir, 'yolo_format')
    os.makedirs(output_dir, exist_ok=True)

    # Iterating through the images 
    for file in files:
        # Loading json file 
        with open(os.path.join(path_to_coco, file), 'r') as f:
            coco = json.load(f)
        
        # Extracting the information about the images that were labeled 
        images = coco.get('images', [])

        # Creating a list off coordinates in the yolo format 
        yolo_format = []
        for annotation in coco.get('annotations', []):
            segment = annotation['segmentation'][0]
            class_id = annotation['category_id']
            image_id = annotation['image_id']

            # Creating a string for the yolo file 
            yolo_string = f'{class_id} {" ".join([str(x) for x in segment])}'

            # Creating the dict entry 
            entry = {
                image_id: yolo_string,
            }

            # Appending the yolo string 
            yolo_format.append(entry)
        
        # Iterating over the images and saving the labels for the images
        for image in images:
            # Getting the image id 
            img_id = image['id']

            # Getting the image name 
            img_name = image['file_name']
            img_name = os.path.basename(img_name)

            # Extracting all the entries in the list of yolo format 
            # that correspond to the image id
            image_yolo_format = [x.get(img_id) for x in yolo_format]
            image_yolo_format = [x for x in image_yolo_format if x is not None]

            # Changing the image ending format to .txt 
            img_name = re.sub(r'.jpg|.png|.jpeg', '.txt', img_name)

            # Creating a .txt file in the output dir for the image 
            with open(os.path.join(output_dir, img_name), 'w') as f:
                f.write('\n'.join(image_yolo_format))

