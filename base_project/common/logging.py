"""Logger class.

Log running processes.
"""
# Author: Dongjin Yoon <djyoon0223@gmail.com>

from base_project.common.utils import *


class LoggerFactory(metaclass=MetaSingleton):
    """Logger Factory.

    Examples:
        >>> from base_project.common.logging import log, dlog
        >>> log("This is printed always")
        >>> dlog("This is printed only when", "debug=True")
    """
    def __init__(self):
        # Stdout handler
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG if self.debug else logging.INFO)

        # File handler
        file_handler = logging.FileHandler(filename=self.log_path)
        file_handler.setLevel(logging.DEBUG)

        # Merge handlers
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

        # Exception handling
        sys.excepthook = lambda *args: logger.error("\nUncaught exception:", exc_info=args)
        self.logger = logger

    @classmethod
    def set(cls, args):
        log_dir = yaml2dict(args.configs)['log_dir']
        cls.log_path = join(log_dir, f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%s')}.log")
        os.makedirs(log_dir, exist_ok=True)
        cls.debug = args.debug


log  = lambda *msgs: LoggerFactory().logger.info(' '.join(lmap(str, msgs)))
dlog = lambda *msgs: LoggerFactory().logger.debug(' '.join(lmap(str, msgs)))
