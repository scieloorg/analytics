#!/usr/bin/env python3
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

install_requires = [
    'requests',
    'cython',
    'thriftpy2',
    'pyramid',
    'pyramid_chameleon',
    'pyramid_mako',
    'pyramid_debugtoolbar',
    'waitress',
    'Babel',
    'dogpile.cache',
    'pylibmc',
    'scieloh5m5',
    'xylose',
    'articlemetaapi',
    'publicationstatsapi',
    'scielojcr',
    'altmetric'
    ]

setup(
    name="analytics",
    version='2.3.0',
    description="A analytics frontend for SciELO usage and publication statistics",
    author="SciELO",
    author_email="scielo-dev@googlegroups.com",
    license="BSD 2-clause",
    url="http://docs.scielo.org",
    keywords='scielo statistics',
    packages=['analytics'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.13",
        "Operating System :: POSIX :: Linux",
        "Topic :: System",
        "Topic :: Services",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    message_extractors={
        'analytics': [
            ('**.py', 'python', None),
            ('templates/**.html', 'mako', None),
            ('templates/**.mako', 'mako', None),
            ('static/**', 'ignore', None)
        ]
    },
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.13,<4",
    extras_require={"test": ["coverage"]},
    install_requires=install_requires,
    entry_points="""\
    [paste.app_factory]
    main = analytics:main
    """,
)
