from pathlib import Path

from pydantic import BaseModel

LOG_FOLDER = "/var/logs/pylogs"
path = Path(LOG_FOLDER)
path.mkdir(parents=True, exist_ok=True)


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "mycoolapp"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"
    LOG_FILE: str = LOG_FOLDER + "/demo-api.log"

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "file": {
            "formatter": "default",
            "class": "logging.FileHandler",
            "filename": LOG_FILE,
        },
    }
    loggers = {
        "demo-api": {"handlers": ["default", "file"], "level": LOG_LEVEL},
    }
