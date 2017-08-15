# -*- coding: utf-8 -*-
import os
import requests
from utils import generate_signature, now
from jinja2 import Environment, FileSystemLoader


basedir = os.path.dirname(os.path.abspath(__file__))


class SmsClient(object):
    def __init__(self, login, api_key, sender='REDSMS.RU'):
        self.gateway = 'https://lk.redsms.ru/get/'
        self.login = login
        self.api_key = api_key
        self.sender = sender
        self.timestamp = None
        self.__token = ''                                                         # deprecated
        template_dir = '/'.join([basedir, 'templates'])                           # deprecated
        self.__template_env = Environment(loader=FileSystemLoader(template_dir))  # deprecated

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

    def __call(self, template_filename, context):
        context['security_token'] = self.__token
        context['sender'] = self.sender
        template = self.__template_env.get_template(template_filename)
        request = template.render(context)
        headers = {'Content-Type': 'text/xml; charset=utf-8'}
        r = requests.post(self.gateway, headers=headers, data=request.encode('utf-8'))
        return r.content

    def send(self, to, message):
        context = {
            'to': to,
            'message': message.decode('utf-8'),
        }
        response = self.__call('message.xml', context)
        print response
