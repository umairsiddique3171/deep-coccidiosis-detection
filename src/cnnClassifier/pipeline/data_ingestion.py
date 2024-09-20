from src.cnnClassifier.config.configuration import *
from src.cnnClassifier.components.data_ingestion import *
from src.cnnClassifier.logger import logging
from src.cnnClassifier.exception import CustomException


class DataIngestionTrainingPipeline:

    def __init__(self):
        self.STAGE_NAME = "Data Ingestion Stage"

    def main(self):
        try: 
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.copy_or_download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise CustomException(e,sys)
        
        
if __name__ == "__main__":
    try: 
        obj = DataIngestionTrainingPipeline()
        logging.info(f'"{obj.STAGE_NAME}" started')
        obj.main()
        logging.info(f'"{obj.STAGE_NAME}" completed')
    except Exception as e:
        raise CustomException(e,sys)