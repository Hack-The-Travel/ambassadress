# -*- coding: utf-8 -*-
"""
ambassadress._internal_utils
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Provides utility functions that are consumed internally by ambassadress.
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


def generate_secret(ts, api_key):
    """Return secret for simple RedSMS auth.

    https://cp.redsms.ru/reference/api#auth

    :param ts: value of request header `ts` field
    :type ts: str
    :param api_key: API key, it can be configured in the settings (https://cp.redsms.ru/settings/)
    :type api_key: str
    :returns: value for request header `secret` field
    :rtype: str
    """
    return md5(ts + api_key).hexdigest()
