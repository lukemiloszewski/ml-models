FROM python:3.9

WORKDIR /code

COPY ./src/ml_models /code/ml_models
COPY ./requirements.txt /code/requirements.txt
COPY ./scripts/main.py /code/main.py

RUN apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
        cmake \
        unzip \
        yasm \
        pkg-config \
        libswscale-dev \
        libtbb2 \
        libtbb-dev \
        libjpeg-dev \
        libpng-dev \
        libtiff-dev \
        libopenjp2-7-dev \
        libavformat-dev \
        libpq-dev \
        libgl1-mesa-glx

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
