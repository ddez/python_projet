import logging
import getpass

class UserFilter(logging.Filter):
    def filter(self, record):
        record.user = getpass.getuser()
        return True

def setup_logger():
    """
    Configure and setup the logging system.
    Returns the root logger with proper configuration.
    """
    # Create formatter first
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(levelname)s - %(user)s - %(name)s - %(message)s',
        datefmt='%Y-%m-%dT%H:%M:%S%z'
    )

    # Create file handler
    file_handler = logging.FileHandler('gestmun.log', encoding='utf-8')
    file_handler.setFormatter(formatter)
    
    # Create and configure the user filter
    user_filter = UserFilter()
    file_handler.addFilter(user_filter)

    # Configure the root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)
    
    return root_logger