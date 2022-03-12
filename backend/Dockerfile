FROM python:3.9

RUN apt-get update && apt-get install libgl1-mesa-glx -y --no-install-recommends

COPY ./scripts/main.py /main.py
COPY ./start.sh /start.sh
COPY ./gunicorn_conf.py /gunicorn_conf.py

RUN chmod +x /start.sh

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./src/ml_models /ml_models
WORKDIR /ml_models

ENV PYTHONPATH=/ml_models

EXPOSE 80

CMD ["/start.sh"]
