import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox   
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML file and return its content as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty or not properly formatted.")
    except Exception as e:
        logger.error(f"Error reading YAML file {path_to_yaml}: {e}")
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """
    Create directories if they do not exist.

    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool): If True, log the creation of directories.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save json data to a file.

    Args:
        path (Path): Path to save the JSON file.
        data (dict): Data to be saved in JSON format.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"JSON file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load JSON data from a file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Content of the JSON file as a ConfigBox object.
    """
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"JSON file loaded from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary data to a file.

    Args:
        data (Any): Data to be saved in binary format.
        path (Path): Path to save the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary data from a file.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Content of the binary file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in KB.

    Args:
        path (Path): Path to the file.

    Returns:
        str: Size of the file in a KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"


def decodeImage(imgstring, filename):
    """
    Decodes a base64 encoded image string and saves it to a file.

    Args:
        imgstring (str): Base64 encoded image string.
        filename (str): Name of the file to save the decoded image.
    """
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
    logger.info(f"Image saved as: {filename}")       


def encodeImageIntoBase64(cropped_image_path):
    """
    Encodes an image file into a base64 string.

    Args:
        cropped_image_path (str): Path to the image file.
    """
    with open(cropped_image_path, "rb") as image_file:
        return base64.b64encode(image_file.read())
    

