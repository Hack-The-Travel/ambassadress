# -*- coding: utf-8 -*-
import os
import requests
from jinja2 import Environment, FileSystemLoader


basedir = os.path.dirname(os.path.abspath(__file__))


class SmsClient(object):
    def __init__(self, login, api_key, sender='REDSMS.RU'):
        self.__gateway = 'http://lik.redsms.ru/'
        self.__login = login
        self.__api_key = api_key
        self.__sender = sender
        self.__token = ''                                                         # deprecated
        template_dir = '/'.join([basedir, 'templates'])                           # deprecated
        self.__template_env = Environment(loader=FileSystemLoader(template_dir))  # deprecated

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
