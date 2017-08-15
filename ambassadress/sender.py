# -*- coding: utf-8 -*-
import os
import requests
from utils import generate_signature, now
from jinja2 import Environment, FileSystemLoader


basedir = os.path.dirname(os.path.abspath(__file__))


class SmsClient(object):
    def __init__(self, login, api_key, sender='REDSMS.RU'):
        self.__gateway = 'https://lk.redsms.ru/get/'
        self.__login = login
        self.__api_key = api_key
        self.__sender = sender
        self.__timestamp = None
        self.__token = ''                                                         # deprecated
        template_dir = '/'.join([basedir, 'templates'])                           # deprecated
        self.__template_env = Environment(loader=FileSystemLoader(template_dir))  # deprecated

    def _sync_time(self):
        """Set __timestamp property."""
        self.__timestamp = now()
        return self.__timestamp

    def _call(self, service, params=None):
        if params is not None:
            request_params = params.copy()
        else:
            request_params = dict()
        request_params['login'] = self.__login
        request_params['timestamp'] = self._sync_time()
        signature = generate_signature(request_params, self.__api_key)
        request_params['signature'] = signature
        r = requests.get(self.__gateway + service, params=request_params)
        return r.content

    def __call(self, template_filename, context):
        context['security_token'] = self.__token
        context['sender'] = self.__sender
        template = self.__template_env.get_template(template_filename)
        request = template.render(context)
        headers = {'Content-Type': 'text/xml; charset=utf-8'}
        r = requests.post(self.__gateway, headers=headers, data=request.encode('utf-8'))
        return r.content

    def send(self, to, message):
        context = {
            'to': to,
            'message': message.decode('utf-8'),
        }
        response = self.__call('message.xml', context)
        print response
