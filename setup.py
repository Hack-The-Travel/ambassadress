import os
from codecs import open
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

about = dict()
with open(os.path.join(here, 'ambassadress', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=about['__description__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=[
        'ambassadress',
    ],
    license=about['__license__'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests>=2.18.0, <3',
    ],
)
