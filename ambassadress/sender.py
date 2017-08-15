# -*- coding: utf-8 -*-
import requests
from utils import generate_signature, now


class SmsClient(object):
    def __init__(self, login, api_key, sender='REDSMS.RU'):
        self.gateway = 'https://lk.redsms.ru/get/'
        self.login = login
        self.api_key = api_key
        self.sender = sender
        self.timestamp = None

    def _sync_time(self):
        """Set __timestamp property."""
        self.timestamp = now()
        return self.timestamp

    def _call(self, service, params=None):
        if params is not None:
            request_params = params.copy()
        else:
            request_params = dict()
        request_params['login'] = self.login
        request_params['timestamp'] = self._sync_time()
        signature = generate_signature(request_params, self.api_key)
        request_params['signature'] = signature
        r = requests.get(self.gateway + service, params=request_params)
        return r.content

    def get_balance(self):
        print self._call('balance.php')
