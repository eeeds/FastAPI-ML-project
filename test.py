import requests

url = 'http://localhost:8000/predict'

customer = {
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

response = requests.post(url, json=customer).json()

print(response)