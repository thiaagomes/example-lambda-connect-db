
from cmath import log
import logging


class AppLogger:

    def create_logger(self, name: str) -> logging.logger:

        formatter = logging.Formatter('{"Timestamp": "%(asctime)s", "Level": "%(levelname)s", "ApplicationName": "testeLambda"}')
        handler = loggin.StreamHandler()
        handler.setFormatter(formatter)
        logger = logging.getLogger(name)

        if logger.handlers:
            for handler in logger.handlers:
                logger.removeHandler(handler)
        
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        logger.propagate = False
        return logger

    def error(self, message_error):
        pass