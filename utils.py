import logging

# 1:ERROR 2:WARNING 3:INFO 4:DEBUG OTHER:DEBUG
LOGGING_LEVEL=3

def setting_logging():
    if LOGGING_LEVEL == 4:
        logging.basicConfig(level=logging.DEBUG)
    elif LOGGING_LEVEL == 3:
        logging.basicConfig(level=logging.INFO)
    elif LOGGING_LEVEL == 2:
        logging.basicConfig(level=logging.WARNING)
    elif LOGGING_LEVEL == 1:
        logging.basicConfig(level=logging.ERROR)
    else:
        logging.basicConfig(level=logging.DEBUG)