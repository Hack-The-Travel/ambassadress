# -*- coding: utf-8 -*-
"""
ambassadress.utils
~~~~~~~~~~~~~~~~~~

This module provides utility functions that are used within ambassadress
that are also useful for external consumption.
"""

from hashlib import md5


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
