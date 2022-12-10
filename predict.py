from fastapi import FastAPI
import pickle 

model_file = './models/pipeline.bin'

with open(model_file, 'rb') as f_in:
    pipeline = pickle.load(f_in)


app = FastAPI()

@app.post('/predict')
async def predict(customer:dict):
    y_pred = pipeline.predict_proba(customer)[0,1]
    churn = y_pred>=0.5

    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }

    return result 
