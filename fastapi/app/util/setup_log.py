import logging
import os
from datetime import time
from logging import handlers

from app.config.settings import settings
from app.util.enum.server_env import ServerEnv

format_string = "%(asctime)s,%(levelname)s,%(otelTraceID)s,%(pathname)s,%(module)s,%(funcName)s[%(lineno)d]:%(message)s"
date_format = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(format_string, date_format)

def setup_log():
    env = settings.env
    appname = settings.appname

    if env == ServerEnv.LOCAL:
        logger_dir = os.path.join(settings.project_dir, "logs")
    else:
        logger_dir = os.path.join(settings.server_home, "logs", appname)

    # make sure the log directory exists
    os.makedirs(logger_dir, exist_ok=True)

    logger = logging.getLogger()

    # info
    logger.addHandler(create_log_handler(
        os.path.join(logger_dir, f"{appname}-info.log"),
        logging.INFO,
    ))

    # error
    logger.addHandler(create_log_handler(
        os.path.join(logger_dir, f"{appname}-error.log"),
        logging.ERROR,
    ))

    # console
    if env == ServerEnv.LOCAL:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

def create_log_handler(filename: str, level: int) -> handlers.TimedRotatingFileHandler:
    handler = handlers.TimedRotatingFileHandler(
        filename=filename,
        when="D",
        interval=1,
        backupCount=5,
        encoding="utf-8",
        atTime=time(0, 0),
        utc=True,
    )
    handler.suffix = "%Y-%m-%d.log"
    handler.setLevel(level)
    handler.setFormatter(formatter)
    return handler
