from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from typing import Optional
import pandas as pd
import io
import os
import pickle
from datetime import datetime
from flaml import AutoML
import json

router = APIRouter(prefix="/train", tags=["training"])

def detect_problem_type(y: pd.Series) -> str:
    if y.dtype == "object" or y.nunique() <= 10:
        return "classification"
    elif y.dtype in ["int64", "float64"]:
        return "regression"
    else:
        raise ValueError("No se puede determinar el tipo de problema automáticamente.")

@router.post("/")
async def train_model_flaml(
    file: UploadFile = File(...),
    metric: Optional[str] = Query(None, description="Métrica a optimizar (accuracy, r2, etc.)")
):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="El archivo debe ser un CSV.")

    try:
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

        if df.shape[1] < 2:
            raise HTTPException(status_code=400, detail="El CSV debe tener al menos dos columnas.")
        if df.isnull().any().any():
            raise HTTPException(status_code=400, detail="El CSV contiene valores nulos.")

        X = df.iloc[:, :-1]
        y = df.iloc[:, -1]
        task = detect_problem_type(y)

        automl = AutoML()
        settings = {
            "time_budget": 30,  # segundos
            "metric": metric if metric else ("accuracy" if task == "classification" else "r2"),
            "task": task,
            "log_file_name": "ml/train_log_flaml.log",
            "verbose": 0
        }

        automl.fit(X_train=X, y_train=y, **settings)

        # Guardar modelo
        os.makedirs("ml", exist_ok=True)
        with open("ml/model.pkl", "wb") as f:
            pickle.dump(automl.model, f)

        # Guardar log estructurado
        log_info = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "filename": file.filename,
            "model_type": task,
            "best_model": str(automl.model),
            "metric_used": settings["metric"],
            "score": automl.best_loss if task == "regression" else automl.best_score
        }

        with open("ml/train_log.json", "w") as f:
            json.dump(log_info, f, indent=4)

        return {
            "message": f"✅ Modelo {task} entrenado exitosamente con FLAML",
            "model": str(automl.model),
            "metric": settings["metric"],
            "score": log_info["score"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en el entrenamiento: {str(e)}")
