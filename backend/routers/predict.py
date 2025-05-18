
from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel, Field
from typing import List, Union, Dict, Any
import pandas as pd
import pickle
import os
import json

router = APIRouter(prefix="/predict", tags=["prediction"])

# ✅ Modelo de entrada para Swagger y validación
class FeatureRow(BaseModel):
    values: List[Union[float, int]]

class PredictionRequest(BaseModel):
    features: List[FeatureRow] = Field(..., example=[
        {"values": [5.1, 3.5, 1.4, 0.2]},
        {"values": [6.2, 2.8, 4.8, 1.8]}
    ])

class PredictionResponse(BaseModel):
    task: str
    metric: str
    predictions: List[Union[int, float]]

@router.post("/", response_model=PredictionResponse)
def predict_route(request: PredictionRequest = Body(...)):
    model_path = "ml/model.pkl"
    log_path = "ml/train_log.json"

    if not os.path.exists(model_path):
        raise HTTPException(status_code=404, detail="Modelo no encontrado.")
    if not os.path.exists(log_path):
        raise HTTPException(status_code=404, detail="Log de entrenamiento no encontrado.")

    try:
        with open(model_path, "rb") as f:
            model = pickle.load(f)

        with open(log_path, "r") as f:
            log = json.load(f)

        # ✅ Convertimos FeatureRow -> List[List[float]]
        input_data = pd.DataFrame([row.values for row in request.features])

        predictions = model.predict(input_data)

        return PredictionResponse(
            task=log.get("model_type", "desconocido"),
            metric=log.get("metric_used", "N/A"),
            predictions=predictions.tolist()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al predecir: {str(e)}")
