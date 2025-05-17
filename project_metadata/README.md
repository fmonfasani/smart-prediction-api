# 🧠 smart-prediction-api

Este proyecto integra un modelo de Machine Learning entrenado en Python con un contrato inteligente en Solidity, a través de una API REST construida con FastAPI.

## 🚀 Cómo iniciar

### 1. Crear entorno virtual

En PowerShell o CMD:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r backend/requirements.txt
```

### 2. Entrenar el modelo

```bash
python ml/train_model.py
```

### 3. Levantar el backend

```bash
uvicorn backend.app:app --reload --port 8080
```

### 4. Acceder a Swagger

`http://localhost:8080/docs`

## 📦 Estructura principal

- `backend/`: FastAPI + JWT + CRUD
- `ml/`: entrenamiento del modelo
- `contract/`: contrato Solidity + deploy
- `test/`: pruebas automatizadas

