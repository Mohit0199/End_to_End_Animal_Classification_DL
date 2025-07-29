from dataclasses import dataclass
from pathlib import Path

# This entity contains the configuration for data ingestion in the CNN Classifier project.
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path