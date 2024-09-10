import pickle
from app.models import HouseFeatures
import pandas as pd
from model.preprocess import preprocess_input
with open('./model/housing_model.pkl','rb') as f:
    model = pickle.load(f)
# Load the preprocessor
with open('./model/preprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)
def preprocess_input(df):
    # Use the preprocessor from training
    return preprocessor.transform(df)   
def predict_price(features:HouseFeatures)->float:
    df = pd.DataFrame([features.model_dump()])
    df = preprocess_input(df)
    prediction = model.predict(df)[0]
    return prediction

