from src.cellSegmentation.logger import logging 
from src.cellSegmentation.exception import AppException
import sys

logging.info("welcome")

try:
    a=4/"6"
except Exception as e:
    raise AppException(e,sys)
    