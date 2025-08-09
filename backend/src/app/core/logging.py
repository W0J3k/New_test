import logging


LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


def init_logging() -> None:
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
