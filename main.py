from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel
import joblib

# Load your model here
model = joblib.load('model/model.pkl')

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
    num: int

app = FastAPI()

@app.post("/predict")
async def predict(item: Item):
    # One-hot encode categorical features
    encoded_sex = 1 if item.sex == "Male" else 0
    encoded_dataset = 1 if item.dataset == "Cleveland" else 0
    encoded_cp = 1 if item.cp == "typical angina" else 0
    encoded_restecg = 1 if item.restecg == "lv hypertrophy" else 0
    encoded_slope = 1 if item.slope == "downsloping" else 0
    
    # Prepare input data
    data = [
        item.id, item.age, encoded_sex, encoded_dataset, encoded_cp,
        item.trestbps, item.chol, item.fbs, encoded_restecg, item.thalch,
        item.exang, item.oldpeak, encoded_slope, item.num
    ]
    
    # Convert data to numpy array
    data_array = np.array(data).reshape(1, -1)
    prediction = model.predict(data)
    return {"prediction": prediction}

@app.get("/")
def read_root():

    return {"Hello": "World"}