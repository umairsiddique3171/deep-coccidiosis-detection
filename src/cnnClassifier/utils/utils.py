import sys
import os
import yaml
import json
import base64
import pandas as pd 
import numpy as np
import joblib
import tensorflow as tf
from pathlib import Path
from box import ConfigBox
from typing import Any
from ensure import ensure_annotations
from src.cnnClassifier.constants import HOME
from src.cnnClassifier.logger import logging
from src.cnnClassifier.exception import CustomException


@ensure_annotations
def read_yaml(path:Path,home=HOME) -> ConfigBox:
    try: 
        file_path = Path(os.path.join(home,path))
        with open(file_path) as file:
            content = yaml.safe_load(file)
        logging.info(f"yaml file loaded successfully form: {file_path}")
        return ConfigBox(content)
    except Exception as e:
        raise CustomException(e,sys)
    

@ensure_annotations
def load_json(path:Path,home=HOME) -> ConfigBox:
    try:
        file_path = Path(os.path.join(home,path)) 
        with open(file_path) as f:
            content = json.load(f)
        logging.info(f"json file loaded succesfully from: {file_path}")
        return ConfigBox(content)
    except Exception as e: 
        raise CustomException(e,sys)
    

@ensure_annotations
def load_bin(path:Path,home=HOME) -> Any:
    try: 
        file_path = Path(os.path.join(home,path))
        data = joblib.load(file_path)
        logging.info(f"binary file loaded from: {file_path}")
        return data
    except Exception as e: 
        raise CustomException(e,sys)
    


@ensure_annotations
def create_directories(path_to_directories: list,home=HOME, verbose=True):
    try:
        for path in path_to_directories:
            dir_path = Path(os.path.join(home,path))
            if not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)
                if verbose:
                    logging.info(f"created directory at: {dir_path}")
            else:
                logging.info(f"directory already exists at: {dir_path}")
    except Exception as e : 
        raise CustomException(e,sys)


@ensure_annotations
def save_json(path: Path, data: dict, home=HOME):
    try: 
        file_path = Path(os.path.join(home,path))
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        logging.info(f"json file saved at: {file_path}")
    except Exception as e: 
        raise CustomException(e,sys)


@ensure_annotations
def save_bin(data: Any, path: Path, home=HOME):
    try: 
        file_path = Path(os.path.join(home,path))
        joblib.dump(value=data, filename=file_path)
        logging.info(f"binary file saved at: {file_path}")
    except Exception as e: 
        raise CustomException(e,sys)
    

@ensure_annotations
def get_size(path: Path,home=HOME) -> str:
    try: 
        file_path = Path(os.path.join(home,path))
        size_in_kb = round(os.path.getsize(file_path)/1024)
        return f"~ {size_in_kb} KB"
    except Exception as e: 
        raise CustomException(e,sys)
    

def encodeImageIntoBase64I(path:Path,home=HOME):
    try: 
        file_path = Path(os.path.join(home,path))
        with open(file_path, "rb") as f:
            img_str = base64.b64encode(f.read())
            return img_str
    except Exception as e:
        raise CustomException(e,sys)


def decodeImage(img_str, path:Path,home=HOME):
    try: 
        img = base64.b64decode(img_str)
        file_path = Path(os.path.join(home,path))
        with open(file_path, 'wb') as f:
            f.write(img)
            f.close()
    except Exception as e: 
        raise CustomException(e,sys)
        
