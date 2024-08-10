from logging import Logger, getLogger, DEBUG, StreamHandler, Formatter
import sys

log_level = DEBUG

def get_logger(name: str) -> Logger:
    logger = getLogger(name)
    logger.setLevel(log_level)
    stream_hanlder = StreamHandler(sys.stdout)
    log_formatter = Formatter("%(levelname)s:\t  %(asctime)s %(name)s: %(message)s")
    stream_hanlder.setFormatter(log_formatter)
    logger.addHandler(stream_hanlder)

    return logger