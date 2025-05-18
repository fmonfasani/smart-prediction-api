from fastapi import FastAPI
from backend.routers import auth, users, logs, database, train, predict
from backend.routers.database import engine, Base 
from backend.models import models_user

models_user.Base.metadata.create_all(bind=database.engine)

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Smart ML API",
    description="Entrenamiento y predicción automática con FLAML",
    version="1.0",
    docs_url="/docs",             # Swagger UI
    redoc_url="/redoc",           # Redoc opcional
    openapi_url="/openapi.json"   # Ruta al schema
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(logs.router)
app.include_router(train.router)
app.include_router(predict.router)
@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}