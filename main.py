from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load your model and preprocessor
model = joblib.load('model/model.pkl')
scaler = joblib.load('model/scaler.pkl')

# Define the input schema
class Item(BaseModel):
    id: int
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

@app.post("/predict")
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
    prediction = model.predict(preprocessed_data)

    # Return the prediction
    return {"prediction": prediction.tolist()}