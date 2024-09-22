import os 
from pathlib import Path

HOME = Path("c:/Users/US593/OneDrive/Desktop/deep-coccidiosis-detection")  # working directory

CONFIG_FILE_PATH = Path(os.path.join(os.getcwd(),"config/config.yaml"))
PARAMS_FILE_PATH = Path(os.path.join(os.getcwd(),"params.yaml"))