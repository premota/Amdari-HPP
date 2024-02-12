from src.data_preprocessing.data_ingestion import *
from src.data_preprocessing.data_transformation import *
from src.modeling.training_pipeline import *



if __name__ == "__main__":
    try:
        #data ingestion
        ingestion_obj = DataCollection()
        df = ingestion_obj.initiate_data_collection()

        #data transformation
        transform_obj = DataTransformation()
        train_df, test_df = transform_obj.initiate_data_transformation(df)

        #train model
        model_trainer_obj = ModelTrainer()
        model_trainer_obj.initiate_model_trainer(train_df, test_df, "median_house_value")


    except Exception as e:
        raise CustomException(e,sys)