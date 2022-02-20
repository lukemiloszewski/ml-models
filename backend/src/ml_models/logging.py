import logging
import sys

_DEFAULT_LOG_FORMAT = "%(asctime)s|%(levelname)s|%(thread)d|%(module)s|%(message)s"


def configure_logging():
    console_formatter = logging.Formatter(_DEFAULT_LOG_FORMAT)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(console_formatter)

    logger = logging.getLogger()

    logger.setLevel(logging.INFO)
    logger.addHandler(console_handler)
