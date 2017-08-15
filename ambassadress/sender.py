# -*- coding: utf-8 -*-
import requests
import json
from _internal_utils import generate_signature, now


class SmsClient(object):
    def __init__(self, login, api_key, sender='REDSMS.RU'):
        self.gateway = 'https://lk.redsms.ru/get/'
        self.login = login
        self.api_key = api_key
        self.sender = sender

    def _call(self, service, params=None):
        if params is not None:
            request_params = params.copy()
        else:
            request_params = dict()
        request_params['login'] = self.login
        request_params['timestamp'] = now()
        signature = generate_signature(request_params, self.api_key)
        request_params['signature'] = signature
        r = requests.get(self.gateway + service + '.php', params=request_params)
        return json.loads(r.content)

    def get_balance(self):
        return self._call('balance')['money']

    def send(self, to, message):
        params = {
            'sender': self.sender,
            'phone': to,
            'text': message,
        }
        self._call('send', params=params)
