import logging

def setup_logger():
    logger = logging.getLogger("ETL_Pipeline")
    logger.setLevel(logging.INFO)

    # Prevent duplicate logs
    if not logger.handlers:

        # File handler
        file_handler = logging.FileHandler("etl.log")
        
        # Console handler
        console_handler = logging.StreamHandler()

        # Format
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger


# Global logger (import anywhere)
logger = setup_logger()