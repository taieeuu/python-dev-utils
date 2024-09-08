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

# 查看目前的logging狀態
def show_logger_info():
    # 取得目前所有的 Logger 名稱
    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    
    # 查看根 Logger 的資訊
    print(f"Root logger level: {logging.getLogger().level}")
    print(f"Root logger handlers: {[type(handler).__name__ for handler in logging.getLogger().handlers]}")
    
    # 列出所有 Logger 的詳細資訊
    for logger in loggers:
        print(f"\nLogger: {logger.name}")
        print(f"  Level: {logging.getLevelName(logger.level)}")
        print(f"  Handlers: {[type(handler).__name__ for handler in logger.handlers]}")
        for handler in logger.handlers:
            print(f"    Handler: {type(handler).__name__}, Level: {logging.getLevelName(handler.level)}")
            if isinstance(handler, logging.FileHandler):
                print(f"    Log File: {handler.baseFilename}")