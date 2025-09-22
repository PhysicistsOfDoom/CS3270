import logging
import os

def setup_logger():
    """
    This function sets up a logger that writes logs to 'app.log'.
    The logger is configured to log messages at the DEBUG level and above.
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create custom logger
    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.DEBUG)

    # Prevent adding handlers multiple times
    if not logger.handlers:
        # Build relative path for logs directory
        log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
        os.makedirs(log_dir, exist_ok=True)  # Ensure the logs directory exists
        log_file_path = os.path.join(log_dir, 'app.log')
        # Handler
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.DEBUG)

        # Format logs
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)

        # Add handler
        logger.addHandler(file_handler)

    return logger
