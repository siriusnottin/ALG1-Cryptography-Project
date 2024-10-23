#!/usr/bin/env python3

# Import standard libraries
import logging
import os

from colorlog import ColoredFormatter

# Initialize log
log = logging.getLogger(__name__)
# Set log level
log_level = os.getenv("LOG_LEVEL", "INFO")
try:
    log.setLevel(log_level.upper())
except ValueError:
    log.setLevel(logging.INFO)
    log.error("Invalid log level: %s. Defaulting to INFO.", log_level)
stream_handler = logging.StreamHandler()
formatter = ColoredFormatter(
    " %(module)s: %(asctime)s [%(levelname)s] %(log_color)s %(message)s (%(pathname)s:%(lineno)d)",
    datefmt="%Y-%m-%d %H:%M:%S",
)
stream_handler.setFormatter(formatter)
log.addHandler(stream_handler)

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, os.pardir))

DATA_DIR = os.path.join(PROJECT_ROOT, os.getenv("DATA_DIR", "data"))

if __name__ == "__main__":
    try:
        log.info("Starting the program")
        log.info("Program finished")
    except Exception as e:
        log.exception("Something went wrong: %s", e)
