# -*- coding: utf-8 -*-
import requests
import json
from _internal_utils import generate_signature, now, generate_secret
import uuid


class SmsClient(object):
    def __init__(self, login, api_key, sender='REDSMS.RU'):
        self.gateway = 'https://cp.redsms.ru/api'
        self.login = login
        self.api_key = api_key
        self.sender = sender

    def _call(self, service, params=None):
        ts = str(uuid.uuid4())  # use UUID as unique value instead of time stamp
        headers = {
            'Content-type': 'application/json',
            'login': self.login,
            'ts': ts,
            'secret': generate_secret(ts, self.api_key),
        }
        request_params = params.copy() if params is not None else {}
        r = requests.post(self.gateway + service, headers=headers, json=request_params, verify=False)
        r.raise_for_status()
        return json.loads(r.content)

    def get_balance(self):
        return self._call('balance')['money']

    def send(self, to, message):
        params = {
            'from': self.sender,
            'to': to,
            'text': message,
        }
        self._call('/message', params=params)
