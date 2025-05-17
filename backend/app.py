from fastapi import FastAPI
from routers import auth, users, predictions, logs
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="smart-prediction-api", docs_url="/docs")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(predictions.router)
app.include_router(logs.router)
