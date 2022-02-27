from pydantic import BaseModel


class MnistRequest(BaseModel):
    img_str: str
