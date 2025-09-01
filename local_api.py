import json

import requests
import fastapi
from fastapi.testclient import TestClient
from main import app



client = TestClient(app)

# TODO: send a GET using the URL http://127.0.0.1:8000
r = client.get("http://127.0.0.1:8000")

# TODO: print the status code
print(r.status_code)
# TODO: print the welcome message
print(r.json())



data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# TODO: send a POST using the data above
r = client.post("http://127.0.0.1:8000/data/", json=data)

# TODO: print the status code
print(r.status_code)
# TODO: print the result
print(r.json())
