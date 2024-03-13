from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

class Userdata(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalch: int
    exang: int
    oldpeak: int
    slope: int

pickle_in = open("NaiveBayes.pkl","rb")
model = pickle.load(pickle_in)
app  = FastAPI()

@app.post("/")
async def endpoint(data:Userdata):
    df = pd.DataFrame([data.dict().values()], columns=data.dict().keys())
    yhat = model.predict(df)
    num = int(yhat)
    return {"prediction":num}
@app.get("/")
async def getendpoint():
    return {"hello":"world"}