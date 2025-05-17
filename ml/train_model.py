import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
import joblib

# Dataset sintético de 30 features
X, y = make_classification(n_samples=1000, n_features=30, n_informative=15, n_classes=2, random_state=42)
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Guardar modelo entrenado
joblib.dump(model, "model.pkl")
print("Modelo entrenado y guardado como model.pkl")
