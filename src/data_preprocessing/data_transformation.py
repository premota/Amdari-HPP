from dataclasses import dataclass
import os
import sys

from src.utils.logger import logging
from src.utils.exception import CustomException
from src.data_preprocessing.data_ingestion import DataCollection
from src.utils.helper import save_to_pickle

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
import pandas as pd





@dataclass
class Data_transformation_path:
    preprocessor_obj_path = os.path.join("artifacts", "preprocessor_v1.pkl")

class DataTransformation:
    def __init__(self):
        self.Data_transformation_path = Data_transformation_path()

    @staticmethod
    def train_test_partition(df):
        try:
            train_df, test_df = train_test_split(df, test_size = 0.2, random_state=360)

            train_df, test_df = train_df.reset_index(drop = True), test_df.reset_index(drop = True)
            train_size, test_size = train_df.shape, test_df.shape
            logging.info(f"train test split completed, trainsize: {train_size}, test_size: {test_size}")
            return train_df, test_df
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, data_frame):
        try:
            df = data_frame.drop(["median_house_value"], axis =1)
            logging.info("data transformation initated")

            numerical_features = df.select_dtypes(exclude = "object").columns
            categorical_features = df.select_dtypes(include = "object").columns

            numerical_transformer = StandardScaler()
            categorical_transformer = OneHotEncoder(drop= "if_binary")

            #create pipeline
            feature_pipeline  = ColumnTransformer(
                [
                    ("StandardScaler", numerical_transformer, numerical_features),
                    ("onehotencoder", categorical_transformer, categorical_features)
                ]
            )

            #instatiate pca
            num_features = df.shape[1]
            pca = PCA(n_components=num_features, random_state= 360)

            #Define complete pipeline
            pipeline = Pipeline(steps= [
                ("preprocessor",feature_pipeline ),
                ("pca", pca)
            ]

            )

            data_array = pipeline.fit_transform(df)
            save_to_pickle(self.Data_transformation_path.preprocessor_obj_path, pipeline)
            logging.info("data has been transformed")

            transformed_df = pd.DataFrame(data_array)
            transformed_df  =transformed_df.iloc[:,:6]

            transformed_df["median_house_value"] = data_frame["median_house_value"]
            logging.info(f"dimension reduced to {transformed_df.shape}, features are {transformed_df.columns.to_list()}")
            logging.info("transformation and pca process completed")

            train_df, test_df = DataTransformation.train_test_partition(transformed_df)

            return train_df, test_df

        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    try:
        ingestion_obj = DataCollection()
        df = ingestion_obj.initiate_data_collection()

        transform_obj = DataTransformation()
        train_df, test_df = transform_obj.initiate_data_transformation(df)
    except Exception as e:
        raise CustomException(e,sys)