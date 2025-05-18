from fastapi import APIRouter

router = APIRouter(prefix="/logs", tags=["logs"])

@router.get("/logs")
def get_logs():
    return {"logs": ["log1", "log2"]}
