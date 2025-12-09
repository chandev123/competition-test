# Duality AI & Lunate AI Geospatial Object Detection

This repository contains the codebase for the **Duality AI & Lunate AI Geospatial Object Detection** Kaggle competition. The goal is to detect **Buildings** and **Vehicles** in geospatial imagery.

## 📂 Project Structure

- **`scripts/`**: Contains the core Python scripts for training, inference, and submission generation.
  - `train.py`: Fine-tunes the YOLOv8 model.
  - `predict.py`: Runs inference on test images.
  - `convert_preds_to_csv.py`: Converts YOLO prediction labels to Kaggle's CSV format.
  - `yolo_params.yaml`: Configuration file for dataset paths and class names.
- **`Output_1/`**: Directory containing the training and validation datasets.
- **`testImages/`**: Directory containing images for inference/testing.

## 🚀 Workflow

### 1. Environment Setup
Check your environment (PyTorch, GPU, YOLO) by running:
```bash
python test1.py
```

### 2. Configuration (`yolo_params.yaml`)
Ensure your dataset paths are correctly set in `scripts/yolo_params.yaml`.
For multiple datasets (Output_1, Output_2...), use a list format:
```yaml
train: [
  "C:/path/to/Output_1/.../train/images",
  "C:/path/to/Output_2/.../train/images"
]
val: [
  "C:/path/to/Output_1/.../val/images",
  "C:/path/to/Output_2/.../val/images"
]
```

### 3. Training (`train.py`)
Train the model using the parameters defined in `yolo_params.yaml`.
```bash
python scripts/train.py
```
- Results (weights) are saved in `scripts/runs/detect/trainX/`.

### 4. Prediction (`predict.py`)
Run inference on the test dataset. You will be asked to select the training run folder (e.g., `train`).
**Note**: This overwrites previous results in `scripts/predictions`. Rename the folder if you wish to keep them.
```bash
python scripts/predict.py
```
- Images with bounding boxes: `scripts/predictions/images/`
- Label text files: `scripts/predictions/labels/`

### 5. Submission (`convert_preds_to_csv.py`)
Generate the final `submission.csv` file for Kaggle.
```bash
python scripts/convert_preds_to_csv.py
```
- Output: `scripts/submission.csv`

## 🛠 Classes
- **0**: Building
- **1**: Vehicle
