from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import joblib
from sklearn.pipeline import Pipeline

# Load your model and preprocessor
model = joblib.load('model/model.pkl')
preprocessor = joblib.load('model/preprocessor.pkl')

# Define the input schema
class Item(BaseModel):
    id: int
    age: int
    sex: str
    dataset: str
    cp: str
    trestbps: float
    chol: float
    fbs: bool
    restecg: str
    thalch: float
    exang: bool
    oldpeak: float
    slope: str

app = FastAPI()

@app.post("/predict")
async def predict(item: Item):
    # Convert the input data into a DataFrame to work with ColumnTransformer
    input_data = pd.DataFrame([item.dict()])

    # Ensure correct data types
    # This step is important because FastAPI converts all boolean values to True/False, but your model might expect 1/0
    input_data['fbs'] = input_data['fbs'].astype(int)
    input_data['exang'] = input_data['exang'].astype(int)
    
    # Preprocess the input data using the loaded preprocessor
    preprocessed_data = preprocessor.transform(input_data)

    # Make a prediction
    prediction = model.predict(preprocessed_data)

    # Return the prediction
    return {"prediction": prediction.tolist()}