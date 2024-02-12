import streamlit as st
import pandas as pd
from src.modeling.prediction_pipeline import PredictionPipeline

st.title("median house price prediction")
st.write("---")

col1, col2 = st.columns([1,2])

housing_median_age = col1.number_input("housing median age", value = 0, format = "%d")
population	 = col1.number_input("population", value=0, format="%d")
median_income	 = col1.number_input("median_income", value=0, format="%d")


total_rooms	 =    col2.number_input("total_rooms", value=0, format="%d")
total_bedrooms	 = col2.number_input("total_bedrooms", value=0, format="%d")	
households		 = col2.number_input("households", value=0, format="%d")	

ocean_proximity = st.selectbox(
    "select one option", 
    ("Coastal", "Non-Coastal")
)

if st.button("GET PREDICTION"):
    data = {"housing_median_age":housing_median_age, "total_rooms":total_rooms,
            "total_bedrooms":total_bedrooms, "population":population,	
            "households":households, "median_income":median_income,
            "ocean_proximity":ocean_proximity}
    
    feature = pd.DataFrame(data, index = [0])

    #initiate prediction
    prediction_obj = PredictionPipeline()
    preds = prediction_obj.initiate_prediction_pipeline(feature)

    st.header("Prediction")
    st.write(preds)