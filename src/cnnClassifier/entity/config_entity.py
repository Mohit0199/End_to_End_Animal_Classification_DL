from dataclasses import dataclass
from pathlib import Path

# This entity contains the configuration for data ingestion in the CNN Classifier project.
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


# This entity contains the configuration for preparing the base model in the CNN Classifier project.
@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int