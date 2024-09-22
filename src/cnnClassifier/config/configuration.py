from pathlib import Path
from src.cnnClassifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig
from src.cnnClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, HOME
from src.cnnClassifier.utils.utils import read_yaml, create_directories


class ConfigurationManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH,params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir = Path(config.root_dir),
            source_url = config.source_url,
            source_local_path= Path(config.source_local_url),
            local_data_file = Path(config.local_data_file),
            unzip_dir = Path(config.unzip_dir)
        )
        return data_ingestion_config

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        create_directories([config.root_dir])
        data_ingestion_config = PrepareBaseModelConfig(
            root_dir = Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )
        return data_ingestion_config