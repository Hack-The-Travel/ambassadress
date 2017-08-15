import re
from codecs import open
from setuptools import setup


with open('ambassadress/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name='ambassadress',
    version=version,
    description='Client to send SMS messages',
    url='https://github.com/Hack-The-Travel/ambassadress',
    author='Sergey Popinevskiy',
    author_email='sergey.popinevskiy@gmail.com',
    license='',
    packages=['ambassadress'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests==2.18.1',
    ],
)
