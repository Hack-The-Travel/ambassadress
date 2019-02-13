# -*- coding: utf-8 -*-
"""
ambassadress._internal_utils
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Provides utility functions that are consumed internally by ambassadress.
"""

from hashlib import md5


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
