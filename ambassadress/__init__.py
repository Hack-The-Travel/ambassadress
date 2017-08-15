# -*- coding: utf-8 -*-

#  _  _   /  _   _   _  _  _/  _  _   _   _
# (/ //) () (/ _)  _)  (/ (/  /  (- _)  _)

from .__version__ import (
    __title__, __description__, __url__, __version__,
    __author__, __author_email__, __license__
)
from .sender import SmsClient

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
