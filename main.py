import sys
from src.cnnClassifier.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.logger import logging
from src.cnnClassifier.exception import CustomException


# DATA INGESTION STAGE
try: 
    obj = DataIngestionTrainingPipeline()
    logging.info(f'"{obj.STAGE_NAME}" started')
    obj.main()
    logging.info(f'"{obj.STAGE_NAME}" completed')
except Exception as e:
    raise CustomException(e,sys)


# PREPARE BASE MODEL STAGE
try: 
    obj = PrepareBaseModelTrainingPipeline()
    logging.info(f'"{obj.STAGE_NAME}" started')
    obj.main()
    logging.info(f'"{obj.STAGE_NAME}" completed')
except Exception as e:
    raise CustomException(e,sys)


