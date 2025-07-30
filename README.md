# End-to-End Cancer Classification Deep Learning Project

## Project Overview
This project implements an end-to-end deep learning pipeline for animal classification using convolutional neural networks (CNN). It leverages DVC (Data Version Control) for pipeline orchestration and data/model versioning, and integrates MLflow with DagsHub for experiment tracking, model versioning, and registry.

The project includes data ingestion, base model preparation, model training, and evaluation stages, all managed through a reproducible DVC pipeline. A Flask web application provides endpoints for training the model and making predictions on input images.

## Features
- Modular pipeline stages for data ingestion, base model preparation, training, and evaluation.
- DVC pipeline for reproducible and versioned machine learning workflows.
- MLflow experiment tracking integrated with DagsHub for model versioning and registry.
- Flask web app for triggering training and serving predictions.
- Support for image augmentation and configurable hyperparameters.

## Setup Instructions
1. Clone the repository.
2. Create and activate a Python virtual environment:
   ```bash
   python -m venv myvenv
   source myvenv/Scripts/activate   # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Install and configure DVC and MLflow if not already installed.
5. Configure DagsHub integration for MLflow experiment tracking and model registry as per your DagsHub account.

## Usage

### Running the Pipeline
The pipeline is managed by DVC and consists of the following stages:
- **data_ingestion**: Ingests and prepares raw data.
- **prepare_base_model**: Prepares the base CNN model (e.g., VGG16) with specified parameters.
- **training**: Trains the model with configurable hyperparameters.
- **evaluation**: Evaluates the trained model and outputs metrics.

To run the entire pipeline, use:
```bash
dvc repro
```

Alternatively, you can trigger training via the Flask web app by sending a GET or POST request to the `/train` endpoint, which runs `dvc repro` internally.

### Making Predictions
Start the Flask app:
```bash
python app.py
```
Upload image and click button this will send a POST request to `/predict` with a JSON payload containing the base64-encoded image:
```json
{
  "image": "<base64-encoded-image>"
}
```
The app will return the predicted classification result.

## Configuration
Pipeline parameters are defined in `params.yaml`, including:
- `IMAGE_SIZE`: Input image size (default: [224, 224, 3])
- `BATCH_SIZE`: Batch size for training (default: 32)
- `EPOCHS`: Number of training epochs (default: 50)
- `AUGMENTATION`: Whether to apply data augmentation (default: True)
- `CLASSES`: Number of output classes (default: 3)
- `LEARNING_RATE`: Learning rate for training (default: 0.00001)
- `INCLUDE_TOP`: Whether to include the top layer in the base model (default: False)
- `WEIGHTS`: Pretrained weights to use (default: imagenet)

## Experiment Tracking and Model Versioning
This project uses MLflow integrated with DagsHub for:
- Tracking experiments and logging metrics.
- Versioning models and managing model registry.
- Collaborating and sharing results via DagsHub platform.

Ensure you have configured MLflow to log to your DagsHub repository as per DagsHub documentation.
