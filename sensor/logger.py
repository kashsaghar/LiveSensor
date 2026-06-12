import logging
import os
import sys
from datetime import datetime

#errors ko console ki jagah file me log karne ke liye
LOG_FILE = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"

logs_path = os.path.join(os.getcwd(),"logs", LOG_FILE)

os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d - %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
    #5 levels of logging are there, debug, info, warning, error, critical
)