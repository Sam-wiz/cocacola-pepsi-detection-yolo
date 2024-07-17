Certainly! Here's a README file based on the colab provided in your repository:

---

# Coca-Cola and Pepsi Logo Detection with YOLOv5

This repository contains a project for detecting Coca-Cola and Pepsi logos using the YOLOv5 object detection algorithm. The project includes datasets for both logos, training scripts, and code for evaluating and testing the trained model.

## Table of Contents
- [Installation](#installation)
- [Dataset Preparation](#dataset-preparation)
- [Training](#training)
- [Evaluation](#evaluation)
- [Testing](#testing)
- [Inference](#inference)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Sam-wiz/cocacola-pepsi-detection-yolo.git
    cd cocacola-pepsi-detection-yolo
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install YOLOv5**

    Follow the instructions to install YOLOv5 from its [official repository](https://github.com/ultralytics/yolov5).

## Dataset Preparation

1. **Download Datasets**

    Download the Coca-Cola and Pepsi datasets and place them in the `data/` directory. Ensure the directory structure is as follows:

    ```
    data/
    ├── coca_cola/
    │   ├── images/
    │   └── labels/
    └── pepsi/
        ├── images/
        └── labels/
    ```

2. **Combine Datasets**

    Use the provided script to combine the datasets into a single dataset with two classes:

    ```bash
    python combine_datasets.py
    ```

3. **Split Dataset**

    Split the combined dataset into training, validation, and testing sets:

    ```bash
    python split_dataset.py
    ```

## Training

1. **Configure Training**

    Edit the `data.yaml` file to configure the paths to the training and validation datasets.

2. **Start Training**

    Train the YOLOv5 model using the following command:

    ```bash
    python train.py --img 640 --batch 16 --epochs 50 --data data.yaml --weights yolov5s.pt
    ```

## Evaluation

1. **Evaluate the Model**

    After training, evaluate the model on the validation set:

    ```bash
    python val.py --data data.yaml --weights runs/train/exp/weights/best.pt
    ```

2. **View Results**

    The evaluation results will be saved in the `runs/val/` directory.

## Testing

1. **Test the Model**

    Test the model on the test set:

    ```bash
    python test.py --data data.yaml --weights runs/train/exp/weights/best.pt
    ```

2. **Generate Output**

    Generate a JSON file with detection timestamps and a video with detected logos highlighted:

    ```bash
    python generate_output.py --data data.yaml --weights runs/train/exp/weights/best.pt --source path/to/video.mp4
    ```

## Inference

1. **Run Inference on Images**

    Run inference on a set of images:

    ```bash
    python detect.py --weights runs/train/exp/weights/best.pt --source path/to/images
    ```

2. **Run Inference on Video**

    Run inference on a video file:

    ```bash
    python detect.py --weights runs/train/exp/weights/best.pt --source path/to/video.mp4
    ```

## Acknowledgements

- [YOLOv5](https://github.com/ultralytics/yolov5) by Ultralytics
- [Coca-Cola](https://www.coca-cola.com/) and [Pepsi](https://www.pepsi.com/) for their logos
