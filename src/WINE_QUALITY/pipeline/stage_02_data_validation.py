from src.WINE_QUALITY.config.configuration import ConfigurationManager
from src.WINE_QUALITY.components.data_validation import Data_Validation
from src.WINE_QUALITY import logger



STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = Data_Validation(config = data_validation_config)
        data_validation.validate_columns()