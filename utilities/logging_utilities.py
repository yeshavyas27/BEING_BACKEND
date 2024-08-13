import logging
import os
#
from datetime import datetime
from typing import Any


class LoggingUtilities:
    def __init__(self):
        self.logger = None
        # debug settings
        debug = eval(os.environ.get("DEBUG", "False"))

        if not debug:
            logging.basicConfig(filename=f'/app/logs/{datetime.now().strftime("%m-%d-%Y")}.log',
                                level=logging.INFO,
                                format='%(levelname)s: [%(asctime)s] [%(pathname)s:%(lineno)d] [%(module)s] [%(funcName)s] [%(name)s] %(message)s')
        else:
            logging.basicConfig(level=logging.DEBUG,
                                format='%(levelname)s: [%(asctime)s] [%(pathname)s:%(lineno)d] [%(module)s] [%(funcName)s] [%(name)s] %(message)s')

    def register_app(self, logger: Any):
        self.logger = logger
