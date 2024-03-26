# API for retreiving data for Heart Disease Prediction

## Overview
Our API serves as a powerful tool for predicting heart disease, leveraging the patient's medical history as input data. It employs a sophisticated ensemble model that combines the strengths of the Random Forest Classifier and the Naive Bayes Classifier, enhanced with AdaBoost. This approach ensures a robust and accurate prediction of heart disease, providing valuable insights for healthcare professionals.

## Setup locally

### Prerequisites
- Python 3.12 or higher
- Pip
- Virtualenv
- Node.js

### Installation
1. Clone the repository
```bash
git clone https://github.com/AnuragThePathak/heart-disease-prediction.git
```
2. Navigate to the project directory
```bash
cd heart-disease-prediction
```
3. Navigate to the fastapi repository and create a virtual environment
```bash
cd  fastapi
python3 -m venv .
```
4. Activate the virtual environment
```bash
source .venv/bin/activate
```
5. Install the required packages
```bash
pip install -r requirements.txt
```
6. Start the fastapi server
```bash
uvicorn main:app --reload
```
7. Open a new terminal and navigate to the project directory
```bash
cd heart-disease-prediction/mui
```
8. Install the required packages
```bash
npm install
```
9. Start the React server
```bash
npm start
```
10. Open your browser and navigate to `http://localhost:3000/`
