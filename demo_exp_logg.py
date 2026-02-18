from src.logger import logging
from src.exception import MyException
import sys

try:
    a=2+"7"
    logging.info("this is info log")
except Exception as e:
    logging.info("this is exception log")
    logging.error("this is error log")
    raise MyException(e,sys) from e