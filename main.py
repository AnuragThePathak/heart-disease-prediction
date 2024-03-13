from fastapi import FastAPI
import numpy as np
import pandas as pd
from pydantic import BaseModel
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import joblib
from sklearn.pipeline import Pipeline

# Load your model here
model = joblib.load('model/model.pkl')

# Define the categorical columns and the preprocessor
categorical_columns = ['sex', 'cp','dataset','fbs','restecg','exang','slope']
preprocessor = joblib.load('model/preprocessor.pkl')

# Create a pipeline that first transforms the data and then applies the model
pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('model', model)])

class Item(BaseModel):
    # Define your input schema here
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
    # Convert the item to a dictionary, get the values, convert to list and reshape it
    data = pd.DataFrame([item.dict()])
    prediction = pipeline.predict(data)
    return {"prediction": prediction}