from fastapi.testclient import TestClient

from predict import app 

client = TestClient(app)


def test_predict():
    data = {
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
    }
    response = client.post('/predict', json=data)
    assert response.status_code == 200