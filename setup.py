import os
from setuptools import setup

from withtool import __version__


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    with open(path, encoding='utf-8') as f:
        return f.read()


setup(
    name='with',
    version=__version__,
    description='A shell context manager',
    long_description=read('README.rst'),
    author='Renan Ivo',
    author_email='renanivom@gmail.com',
    url='https://github.com/renanivo/with',
    keywords='context manager shell command line repl',
    scripts=['bin/with'],
    install_requires=[
        'appdirs==1.4.0',
        'docopt==0.6.2',
        'prompt-toolkit==1.0',
        'python-slugify==1.2.1',
    ],
    packages=['withtool'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
