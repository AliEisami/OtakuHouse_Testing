import logging
import os


class Logger:
    def __init__(self, log_file_path):
        # Ensure the directory exists
        log_dir = os.path.dirname(log_file_path)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logging.basicConfig(filename=log_file_path,
                            level=logging.INFO,
                            format="%(asctime)s - %(levelname)s - %(message)s",
                            force=True)
        self.logger = logging.getLogger()

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)


# Usage Example
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../logger.log')
logger = Logger(log_file_path)

logger.info("This is an info message")
logger.error("This is an error message")
