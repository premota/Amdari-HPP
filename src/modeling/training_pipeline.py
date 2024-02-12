from dataclasses import dataclass
import os
import sys

from src.utils.logger import logging
from src.utils.exception import CustomException
from src.utils.helper import save_to_pickle

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score


@dataclass
class model_path:
    trained_model_path  =os.path.join("artifacts", "model_v1.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_config = model_path()
        
    def initiate_model_trainer(self, train_df, test_df, target):
        try:
            logging.info("model training initated")
            X_train, y_train, X_test, y_test = (
                train_df.drop([target], axis =1),
                train_df[target],
                test_df.drop([target], axis =1),
                test_df[target]
            )

            params = {
                    'bootstrap': True,
                    'max_depth': 17,
                    'max_features': 'sqrt',
                    'min_samples_leaf': 4,
                    'min_samples_split': 10,
                    'n_estimators': 107
                    }
            
            logging.info("fitting model")
            rf = RandomForestRegressor(**params)
            model = rf.fit(X_train, y_train)
            
            logging.info("training completed, about to make predictions")
            y_pred = model.predict(X_test)

            save_to_pickle(self.model_config.trained_model_path, model)
            logging.info(f"model saved with R_squared score of {r2_score(y_test, y_pred)}")

        except Exception as e:
            raise CustomException(e,sys)