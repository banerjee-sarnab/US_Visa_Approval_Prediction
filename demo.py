import sys
from US_Visa.logger import logging
from US_Visa.exception import USvisaException


# logging.info("This is our custom log message.")

try:
    a = 1 / 0
except Exception as e:
    raise USvisaException(e, sys)