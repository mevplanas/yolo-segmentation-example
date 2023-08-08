# YOLO segmentation 

Example code for yolo segmentation

# Virtual env creation 

Creating the virtual environment is done using anaconda and the `env.yml` file via the command: 

```
conda env create -f env.yml
```

To update the environment, use the command: 

```
conda env update -f env.yml
```

# Training the segmentation model 

```
python -m train
```

# Predicting on the images in the validation set 

```
python -m predict
```