import json
import logging
import os
from pathlib import Path
import sys
import time

from starlette.requests import Request


_DEFAULT_FORMAT = "%(asctime)s|%(levelname)s|%(thread)d|%(module)s|%(message)s"
_JSON_FORMAT = json.dumps({"time": "%(asctime)s", "level": "%(levelname)s", "module": "%(module)s", "message": "%(message)s"})

def configure_logging(logs_path: Path):
    console_formatter = logging.Formatter(_DEFAULT_FORMAT)
    json_formatter = logging.Formatter(_JSON_FORMAT)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(console_formatter)

    if not logs_path.exists():
        os.makedirs(os.path.dirname(logs_path), exist_ok=True)

    file_handler = logging.FileHandler(logs_path, "a")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(json_formatter)

    logger = logging.getLogger()

    logger.setLevel(logging.INFO)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


async def log_request_metadata(request: Request, call_next):    
    logging.info(f"Request started: type={request.method}, path={request.url.path}")
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()
    duration = "{0:.2f}".format(end_time - start_time)
    logging.info(f"Request finished: status={response.status_code}, duration={duration}s")
    return response
