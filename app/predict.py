from fastapi import FastAPI, HTTPException  
from pydantic import BaseModel


import pickle 

model_file = '../models/pipeline.bin'

with open(model_file, 'rb') as f_in:
    pipeline = pickle.load(f_in)

class Customer(BaseModel):
    CreditScore: int
    Geography: str
    Gender: str
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float
    Exited: int

app = FastAPI()

@app.post('/predict')
async def predict(customer: Customer):
    customer = customer.dict()
    y_pred = pipeline.predict_proba(customer)[0,1]
    churn = y_pred>=0.5

    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }
    if not result:
        raise HTTPException(
        status_code=404, detail=f"There is no result."
    )
    return result 

"""{
  "CreditScore": 597,
  "Geography": "Germany",
  "Gender": "Female",
  "Age": 35,
  "Tenure": 8,
  "Balance": 131101.04,
  "NumOfProducts": 1,
  "HasCrCard": 1,
  "IsActiveMember": 1,
  "EstimatedSalary": 192852.67,
  "Exited": 0
}"""