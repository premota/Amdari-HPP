from dataclasses import dataclass

import sys
import os
import pandas as pd

from src.utils.logger import logging
from src.utils.exception import CustomException

@dataclass
class Data_collection_path:
    clean_data_path = os.path.join("Data", "features.csv")

class DataCollection:
    def __init__(self):
        self.collection_path = Data_collection_path()

    def initiate_data_collection(self):
        logging.info("Data ingestion about to begin")
        try:
            df = pd.read_csv(self.collection_path.clean_data_path)
            logging.info("data has been read, data ingestion completed")

            return df
        except Exception as e:
            raise CustomException(e,sys)