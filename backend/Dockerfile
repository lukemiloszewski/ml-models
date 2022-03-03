FROM python:3.9

WORKDIR /ml_models

COPY ./requirements.txt /ml_models/requirements.txt
COPY ./scripts/main.py /ml_models/main.py

RUN apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
        build-essential \
        cmake \
        git \
        wget \
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
        libpq-dev

RUN pip install --no-cache-dir --upgrade -r /ml_models/requirements.txt
RUN pip install --no-cache-dir git+https://github.com/lukemiloszewski/ml-models@main#subdirectory=backend

RUN apt-get install libgl1-mesa-glx -y

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
