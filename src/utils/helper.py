from src.utils.exception import CustomException
import os
import pickle
import sys

def save_to_pickle(obj_path, obj):
    try:
        dir_path = os.path.dirname(obj_path)
        os.makedirs(dir_path, exist_ok =True )
        with open(obj_path, 'wb') as file:
            pickle.dump(obj, file)
    except Exception as e:
        raise CustomException(e,sys)

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)
