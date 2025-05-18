
import os
import pickle
import pandas as pd
from pycaret.classification import setup as setup_clf, compare_models as compare_clf, save_model as save_clf
from pycaret.regression import setup as setup_reg, compare_models as compare_reg, save_model as save_reg
from pycaret.clustering import setup as setup_clust, create_model as create_clust, save_model as save_clust

def detect_problem_type(df: pd.DataFrame) -> str:
    if df.shape[1] < 2:
        raise ValueError("El dataset debe tener al menos 2 columnas.")
    target = df.iloc[:, -1]
    if target.nunique() < 20 and target.dtype in ['int', 'object']:
        return "classification"
    elif target.dtype in ['int', 'float']:
        return "regression"
    else:
        return "clustering"

def train_model(df: pd.DataFrame, filename: str) -> dict:
    os.makedirs("ml", exist_ok=True)
    target_col = df.columns[-1]
    tipo = detect_problem_type(df)

    if tipo == "classification":
        setup_clf(data=df, target=target_col, silent=True, session_id=123)
        model = compare_clf()
        save_clf(model, "ml/model")
    elif tipo == "regression":
        setup_reg(data=df, target=target_col, silent=True, session_id=123)
        model = compare_reg()
        save_reg(model, "ml/model")
    else:
        setup_clust(data=df, normalize=True, silent=True, session_id=123)
        model = create_clust("kmeans")
        save_clust(model, "ml/model")

    # Guardar CSV con métricas (PyCaret guarda automáticamente)
    df_results = pd.read_csv("logs/Compare Models.csv") if tipo != "clustering" else pd.DataFrame()
    if not df_results.empty:
        df_results.to_csv("ml/evaluation.csv", index=False)

    # Registrar log
    with open("ml/train_log.txt", "a") as f:
        f.write(f"Modelo {tipo} entrenado desde '{filename}' con PyCaret.\n")

    return {
        "status": "success",
        "model_type": tipo,
        "best_model": str(model)
    }
