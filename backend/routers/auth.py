
from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/login")
def login():
    return {"message": "Endpoint de login"}
