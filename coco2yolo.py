# OS traversal 
import os

# JSON reader 
import json 

if __name__ == '__main__': 
    # Infering the current working directory 
    current_dir = os.getcwd()

    # Defining the path to the coco dataset
    path_to_coco = os.path.join(current_dir, 'coco_format')

    # Loading all the images 
    images = os.listdir(os.path.join(path_to_coco))

    # Creating the output directory 
    output_dir = os.path.join(current_dir, 'yolo_format')
    os.makedirs(output_dir, exist_ok=True)

    # Iterating through the images 
    for image in images:
        # Loading json file 
        with open(os.path.join(path_to_coco, image), 'r') as f:
            coco = json.load(f)
        
        # Creating a list off coordinates in the yolo format 
        yolo_format = []
        for annotation in coco.get('annotations', []):
            segment = annotation['segmentation'][0]
            class_id = annotation['category_id']

            # Creating a string for the yolo file 
            yolo_string = f'{class_id} {" ".join([str(x) for x in segment])}'

            # Appending the yolo string 
            yolo_format.append(yolo_string)
        
        # Creating a .txt file in the output dir for the image 
        with open(os.path.join(output_dir, image.replace('.json', '.txt')), 'w') as f:
            f.write('\n'.join(yolo_format))

