
import logging
import sys
from thirdpart.ansistrm import ColorizingStreamHandler
LOGGER = logging.getLogger('w13scan')
LOGGER_HANDLER = ColorizingStreamHandler(sys.stdout)
LOGGER_HANDLER.level_map[logging.getLevelName("*")] = (None, "cyan", False)
LOGGER_HANDLER.level_map[logging.getLevelName("+")] = (None, "green", False)
LOGGER_HANDLER.level_map[logging.getLevelName("-")] = (None, "red", False)
LOGGER_HANDLER.level_map[logging.getLevelName("!")] = (None, "yellow", False)
FORMATTER = logging.Formatter("\r[%(asctime)s] [%(levelname)s] %(message)s", "%H:%M:%S")
LOGGER_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(LOGGER_HANDLER)
LOGGER.setLevel(logging.INFO)
