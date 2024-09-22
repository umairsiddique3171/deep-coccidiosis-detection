import os
import sys
import shutil
import urllib.request as request
from pathlib import Path
import zipfile
from src.cnnClassifier.entity.config_entity import DataIngestionConfig
from src.cnnClassifier.logger import logging
from src.cnnClassifier.exception import CustomException
from src.cnnClassifier.utils.utils import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def copy_or_download_file(self):
        source_file_path = self.config.source_local_path
        try:
            if source_file_path:  # Copy the file if source path is provided
                if os.path.exists(source_file_path):
                    if not os.path.exists(self.config.local_data_file):    
                        shutil.copy2(source_file_path, self.config.local_data_file)
                        logging.info(f"File copied from {source_file_path} to {self.config.local_data_file}")
                    else:
                        logging.info(f"Local file already exists at: {self.config.local_data_file}")
                        logging.info(f"File size: {get_size(Path(self.config.local_data_file))}")
                else:
                    logging.info(f"Source file not found: {source_file_path}")
                    raise FileNotFoundError(f"Source file not found: {source_file_path}")
            else:  # Download the file if it doesn't already exist
                if not os.path.exists(self.config.local_data_file):
                    filename, headers = request.urlretrieve(
                        url=self.config.source_url,
                        filename=self.config.local_data_file
                    )
                    logging.info(f"{filename} downloaded! Info: \n{headers}")
                else:
                    logging.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
        except Exception as e:
            raise CustomException(e, sys)

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        try :
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
        except Exception as e: 
            raise CustomException(e,sys)