import os
from pathlib import Path
import logging

log_str = '[%(asctime)s] - %(levelname)s : %(module)s  : %(message)s'

log_dir = "logs"
logs_filepath = os.path.join(log_dir, "Running_logs.log")
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(level=logging.INFO,
                    format=log_str
                    handlers=[logging.filehandler(logs_filepath),
                              logging.StreamHandler(sys.stdout))
                    ]

logger = logging.getLogger("WINE_QUALITY_LOGGER")

