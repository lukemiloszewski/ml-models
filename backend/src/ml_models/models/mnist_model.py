from pydantic import BaseModel


class MnistRequest(BaseModel):
    data: str


class MnistResponse(BaseModel):
    result: int
