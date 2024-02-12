import pandas as pd
from src.utils.helper import *
from src.utils.exception import CustomException
from src.data_preprocessing.data_transformation import *

import sys
import os


class PredictionPipeline():
    def __init__(self):
        pass

    @staticmethod
    def feature_engineering(data):
        try:
            #create new features
            data["population_per_households"] = data["population"]/data["households"]
            data["rooms_per_household"]  = data["total_rooms"]/data["households"]
            data["bed_rooms_per_household"] = data["total_bedrooms"]/data["households"]
            data["population_per_bedrooms"] = data["population"]/data["total_bedrooms"]
            data["rooms_per_bedrooms"] = data["total_rooms"]/data["total_bedrooms"]

            #drop redundant feature
            data = data.drop(["total_rooms", "total_bedrooms", "households"], axis =1)

            return data
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_prediction_pipeline(self, df):
        try:
            #engineer the features
            data = self.feature_engineering(df)

            # defne path of model and preprocessor
            model_path = os.path.join("artifacts", "model_v1.pkl")
            transformer_path = os.path.join("artifacts", "preprocessor_v1.pkl")

            # Tranform data
            transform_obj  = load_object(transformer_path)
            transformed_df = transform_obj.transform(data)
            transformed_df = pd.DataFrame(daat = transformed_df)

            #select first 6 column
            transformed_df = transformed_df.iloc[:,:6]

            #make prediction
            model = load_object(model_path)
            preds = model.predict(transformed_df)

            return preds
        
        except Exception as e:
            raise CustomException(e,sys)