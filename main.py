from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

# Load your model here
model = joblib.load('model/model.pkl')

# Load the preprocessor
preprocessor = joblib.load('model/preprocessor.pkl')

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

# Load training data
train_data = pd.read_csv('model/preprocessed.csv')

# Identify numeric and categorical columns
numeric_columns = ['age', 'trestbps', 'chol', 'thalch', 'oldpeak']
categorical_columns = ['sex', 'cp', 'dataset', 'restecg', 'slope']

# Initialize SimpleImputer for numeric features
numeric_imputer = SimpleImputer(strategy='mean')

# Initialize SimpleImputer for categorical features
categorical_imputer = SimpleImputer(strategy='most_frequent')

# Initialize OneHotEncoder for categorical features
one_hot_encoder = OneHotEncoder()

# Create a ColumnTransformer to apply different preprocessing steps to numeric and categorical columns
preprocessor = ColumnTransformer(
    transformers=[
        ('numeric', numeric_imputer, numeric_columns),
        ('categorical', one_hot_encoder, categorical_columns)
    ],
    remainder='passthrough'
)

# Fit the ColumnTransformer with training data
preprocessor.fit(train_data)

@app.post("/predict")
async def predict(item: Item):
    # Convert item to a DataFrame
    data = pd.DataFrame(item.dict(), index=[0])
    
    # Preprocess the input data
    preprocessed_data = preprocessor.transform(data)
    
    # Predict using the model
    prediction = model.predict(preprocessed_data)
    return {"prediction": prediction.tolist()}
