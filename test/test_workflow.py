import requests

BASE_URL = "http://localhost:8080"

def test_predict():
    payload = {
        "features": [0.5] * 30
    }
    response = requests.post(f"{BASE_URL}/predict", json=payload)
    print("Predicción:", response.json())

def test_trigger():
    payload = {
        "prediction": 1
    }
    response = requests.post(f"{BASE_URL}/trigger", json=payload)
    print("Trigger contract:", response.text)

def test_status():
    response = requests.get(f"{BASE_URL}/status")
    print("Estado actual del contrato:", response.text)

if __name__ == "__main__":
    test_predict()
    test_trigger()
    test_status()
