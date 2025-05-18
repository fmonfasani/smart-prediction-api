from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

class Prediction(BaseModel):
    input_data: list[float]
    result: float
