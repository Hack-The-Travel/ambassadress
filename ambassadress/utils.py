# -*- coding: utf-8 -*-
"""
ambassadress.utils
~~~~~~~~~~~~~~~~~~

This module provides utility functions that are used within ambassadress
that are also useful for external consumption.
"""

from hashlib import md5
import time


def generate_signature(params, api_key):
    """Generate signature for request to redsms service.

    :param params: dict, parameters dictionary
    :param api_key: str, secret key
    :return: str, generated signature
    """
    params_str = ''
    for key, value in sorted(params.items()):
        params_str += str(value)
    return md5(params_str + api_key).hexdigest()


def now():
    """Returns redsms timestamp.

    The return value is UTC timestamp minus 3 hours.
    Although the documentation says that on the side of the redsms,
    time is set in the UTC.
    """
    three_hours = 3 * 60 * 60
    return int(time.time()) - three_hours
