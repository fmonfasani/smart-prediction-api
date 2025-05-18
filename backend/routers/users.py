
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/users")
def login():
    return {"message": "Endpoint de login"}
