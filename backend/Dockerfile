FROM python:3.9

WORKDIR /code

COPY ./src/ml_models /code/ml_models
COPY ./requirements.txt /code/requirements.txt
COPY ./scripts/main.py /code/main.py

RUN apt-get update
RUN apt-get install libgl1-mesa-glx -y --no-install-recommends

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
