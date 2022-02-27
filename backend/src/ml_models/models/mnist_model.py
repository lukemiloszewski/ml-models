from pydantic import BaseModel


class MnistRequest(BaseModel):
    data: str
