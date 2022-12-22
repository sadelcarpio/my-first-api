from pydantic import BaseModel


class PredictResponse(BaseModel):
    prob: float
    label: str
