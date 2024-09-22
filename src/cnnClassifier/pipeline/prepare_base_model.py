import sys
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.prepare_base_model import PrepareBaseModel
from src.cnnClassifier.logger import logging
from src.cnnClassifier.exception import CustomException


class PrepareBaseModelTrainingPipeline:

    def __init__(self):
        self.STAGE_NAME = "Prepare Base Model Stage"

    def main(self):
        try: 
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.updated_base_model()
        except Exception as e:
            raise CustomException(e,sys)
        
        
if __name__ == "__main__":
    try: 
        obj = PrepareBaseModelTrainingPipeline()
        logging.info(f'"{obj.STAGE_NAME}" started')
        obj.main()
        logging.info(f'"{obj.STAGE_NAME}" completed')
    except Exception as e:
        raise CustomException(e,sys)