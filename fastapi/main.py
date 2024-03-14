from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel
import pandas as pd
import joblib
from fastapi.middleware.cors import CORSMiddleware

# Load your model and preprocessor
scaler = joblib.load('model/scaler.pkl')
rf_model = joblib.load('model/rf_model.pkl')
lr_model = joblib.load('model/lr_model.pkl')
adaboost_model = joblib.load('model/adaboost_model.pkl')

# Define the input schema
class Item(BaseModel):
    age: int
    sex: str
    cp: str
    trestbps: float
    chol: float
    fbs: bool
    restecg: str
    thalch: float
    exang: bool
    oldpeak: float

app = FastAPI()

origins = [
    "http://localhost:3000",  # React app
    "http://localhost:8000",  # FastAPI server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
async def predict(item: Item):
    # Convert the input data into a DataFrame to work with ColumnTransformer
    input_data = pd.DataFrame([item.model_dump()])

    # Ensure correct data types
    # This step is important because FastAPI converts all boolean values to True/False, but your model might expect 1/0
    input_data['fbs'] = input_data['fbs'].astype(int)
    input_data['exang'] = input_data['exang'].astype(int)

    # Convert string datatypes to integer
    input_data['sex'] = input_data['sex'].map({'Male': 1, 'Female': 0})
    input_data['cp'] = input_data['cp'].map({'asymptomatic': 0, 'non-anginal': 1, 'atypical-angina': 2, 'typical-angina': 3})
    input_data['restecg'] = input_data['restecg'].map({'normal': 0, 'lv-hypertrophy': 1, 'st-t-abnormality': 2})

    # Preprocess the input data using the loaded preprocessor
    preprocessed_data = scaler.transform(input_data)

    # Make a prediction
    rf_prediction = rf_model.predict(preprocessed_data)
    lr_prediction = lr_model.predict(preprocessed_data)
    
    # Reshape the predictions to be a 2D array
    predictions = np.array([rf_prediction, lr_prediction]).reshape(1, -1)

    # Use the reshaped predictions as input to the AdaBoost model
    prediction = adaboost_model.predict(predictions)

    # Return the prediction
    return {"prediction": prediction.tolist()}