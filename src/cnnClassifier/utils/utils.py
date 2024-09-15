import sys
import os
import yaml
import json
import base64
import pandas as pd 
import numpy as np
import joblib
import pickle
from pathlib import Path
from box import ConfigBox
from typing import Any
from ensure import ensure_annotations
from src.cnnClassifier.logger import logging
from src.cnnClassifier.exception import CustomException


@ensure_annotations
def read_yaml(path:Path) -> ConfigBox:
    try: 
        with open(path) as file:
            content = yaml.safe_load(file)
            logging.info(f"yaml file : {path} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        raise CustomException(e,sys)
    

@ensure_annotations
def save_json(path:Path,data:dict):
    try: 
        with open(path,"w") as f:
            json.dump(data,f,indent=4)
            logging.info(f"json file save at : {path}")
    except Exception as e :
        raise CustomException(e,sys)


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logging.info(f"created directory at: {path}")
    except Exception as e : 
        raise CustomException(e,sys)


@ensure_annotations
def save_json(path: Path, data: dict):
    try: 
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        logging.info(f"json file saved at: {path}")
    except Exception as e: 
        raise CustomException(e,sys)


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    try: 
        with open(path) as f:
            content = json.load(f)
        logging.info(f"json file loaded succesfully from: {path}")
        return ConfigBox(content)
    except Exception as e: 
        raise CustomException(e,sys)


@ensure_annotations
def save_bin(data: Any, path: Path):
    try: 
        joblib.dump(value=data, filename=path)
        logging.info(f"binary file saved at: {path}")
    except Exception as e: 
        raise CustomException(e,sys)
    

@ensure_annotations
def load_bin(path: Path) -> Any:
    try: 
        data = joblib.load(path)
        logging.info(f"binary file loaded from: {path}")
        return data
    except Exception as e: 
        raise CustomException(e,sys)
    

@ensure_annotations
def get_size(path: Path) -> str:
    try: 
        size_in_kb = round(os.path.getsize(path)/1024)
        return f"~ {size_in_kb} KB"
    except Exception as e: 
        raise CustomException(e,sys)
    

def encodeImageIntoBase64I(img_path):
    try: 
        with open(img_path, "rb") as f:
            img_str = base64.b64encode(f.read())
            return img_str
    except Exception as e:
        raise CustomException(e,sys)


def decodeImage(img_str, file_name):
    try: 
        img = base64.b64decode(img_str)
        with open(file_name, 'wb') as f:
            f.write(img)
            f.close()
    except Exception as e: 
        raise CustomException(e,sys)


def save_object(file_path,obj):
    try :
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path, 'wb') as f:
            pickle.dump(obj, f)
    except Exception as e: 
        raise CustomException(e,sys)
    

def load_object(path):
    try : 
        model = pickle.load(open(path, "rb"))
        return model
    except Exception as e: 
        raise CustomException(e,sys)


def load_selected_features(file_path):
    try:
        with open(file_path,'r') as file_obj:
            features_list = json.load(file_obj)
        return features_list
    except Exception as e:
        raise CustomException(e,sys)


def save_report(report,path):
    try: 
        models_training_report = pd.DataFrame(data={
                'models' : report.keys(),
                'training_r2' : [v[0] for v in list(report.values())],
                'testing_r2' : [v[1] for v in list(report.values())]
            })
        models_training_report.to_csv(path,header=True,index=False)   
    except Exception as e: 
        raise CustomException(e,sys)
