import json
import logging
import os
from pathlib import Path
import sys

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
