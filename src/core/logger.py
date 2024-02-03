import os
import enum
import logging
from logging import config
from typing import Optional

from core import settings
from .logger_config import logger_config

logs_dir: str = os.path.join(settings.root_dir, "logs")
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)
config.dictConfig(logger_config)


class LoggerName(enum.Enum):
    ROOT: str = "root"
    MAIN: str = "main"
    DEBUG: str = "debug"


def get_logger(name: Optional[LoggerName] = None) -> logging.Logger:
    if settings.debug:
        return logging.getLogger(LoggerName.DEBUG.value)
    return logging.getLogger(name.value if name is not None else LoggerName.MAIN.value)
