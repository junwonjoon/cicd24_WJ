"""
    Setting up a logger that still works when the app is containerized
    Author: Wolf Paulus (wolf@paulus.com)
"""
from sys import stdout, stderr
import logging.config
import yaml  # PyYAML

try:
    with open('./src/logconfig.yaml', 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
        logger = logging.getLogger("foo_logger")
except OSError as err:
    logger = logging.getLogger('bar_logger')
    logger.setLevel(logging.DEBUG)  # set logger level
    logFormatter = logging.Formatter(
        "%(name)-12s %(asctime)s %(levelname)-8s %(filename)s:%(funcName)s %(message)s")
    consoleHandler = logging.StreamHandler(
        stderr)  # set streamhandler to stderr
    consoleHandler.setFormatter(logFormatter)
    logger.addHandler(consoleHandler)


if __name__ == "__main__":
    logger.debug('This is a debug message')
    logger.warning('This is a warning message')
    logger.error('This is a error message')