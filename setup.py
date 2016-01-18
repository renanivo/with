import os
from setuptools import setup


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    with open(path, encoding='utf-8') as f:
        return f.read()

setup(
    name='with',
    version='0.0.1',
    description='A shell context manager',
    long_description=read('README.md'),
    author='Renan Ivo',
    author_email='renanivom@gmail.com',
    url='https://github.com/renanivo/with',
    keywords='context manager shell command line repl',
    scripts=['bin/with'],
    install_requires=[
        'prompt-toolkit==0.54',
        'appdirs==1.4.0',
    ],
    packages=['withtool'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
    ]
)
