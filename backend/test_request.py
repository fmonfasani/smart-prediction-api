import requests

url = "http://localhost:8000/predict/"
payload = {
    "features": [
        {"values": [5.1, 3.5, 1.4, 0.2]},
        {"values": [6.2, 2.8, 4.8, 1.8]}
    ]
}

response = requests.post(url, json=payload)
print("Status:", response.status_code)
print("Response:", response.json())
