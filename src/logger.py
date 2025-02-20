import logging
import os
from datetime import datetime

# Create a unique log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a directory for logs if it doesn't exist
logs_path = os.path.join(os.getcwd(), 'logs')
os.makedirs(logs_path, exist_ok=True)

# Define the full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Corrected from 'file_name' to 'filename'
    format="%(asctime)s [%(lineno)d] %(name)s - %(levelname)s - %(message)s",  # Corrected format syntax
    level=logging.INFO,
)

# if __name__ == "__main__":
#     logging.info("Logging has started.")
