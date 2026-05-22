#!/usr/bin/env python3
#coding:utf-8
from setuptools import setup, find_packages
import codecs


install_requires = [
    'thriftpy2>=0.4',
]


setup(
    name="thriftpywrap",
    version='0.1.1',
    description="Lib to help you build console based thrift servers.",
    long_description=codecs.open('README.rst', mode='r', encoding='utf-8').read(),
    author="SciELO",
    author_email="scielo-dev@googlegroups.com",
    maintainer="Gustavo Fonseca",
    maintainer_email="gustavo.fonseca@scielo.org",
    license="BSD License",
    url="http://docs.scielo.org",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.13,<4",
    test_suite='tests',
    install_requires=install_requires,
)
