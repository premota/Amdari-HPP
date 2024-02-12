import logging
import os
from datetime import datetime

log_dir_name = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", log_dir_name)
os.makedirs(logs_path, exist_ok = True)

log_file_path = os.path.join(logs_path, "log-file.log")

logging.basicConfig(
    filename= log_file_path,
    format = "[%(asctime)s] %(lineno)d -%(levelname)s - %(message)s",
    level = logging.INFO,
)