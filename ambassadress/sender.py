# -*- coding: utf-8 -*-
import os
import requests
from jinja2 import Environment, FileSystemLoader


basedir = os.path.dirname(os.path.abspath(__file__))


class SmsClient(object):
    def __init__(self, token, sender='REDSMS.ru'):
        self.__token = token
        self.__sender = sender
        self.__gateway = 'https://adm.redsms.ru/xml/'
        template_dir = '/'.join([basedir, 'templates'])
        self.__template_env = Environment(loader=FileSystemLoader(template_dir))

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
