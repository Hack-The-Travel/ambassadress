# -*- coding: utf-8 -*-

#  _  _   /  _   _   _  _  _/  _  _   _   _
# (/ //) () (/ _)  _)  (/ (/  /  (- _)  _)

__title__ = 'ambassadress'
__version__ = '0.0.0'
__author__ = 'Sergey Popinevskiy'

from .sender import SmsClient

# Set default logging handler to avoid "No handler found" warnings.
import logging
try: # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
