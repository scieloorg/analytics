#!/usr/bin/env python
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

install_requires = [
    'requests>=2.7.0',
    'elasticsearch>=1.7.0',
    'cython>=0.22',
    'thriftpy>=0.3.1',
    'thriftpywrap',
    'xylose',
    'pyramid>=1.5.7',
    'pyramid_chameleon',
    'pyramid_mako',
    'pyramid_debugtoolbar',
    'waitress',
    'Babel>=2.0',
    'dogpile.cache>=0.5.6',
    'pylibmc>=1.5.0',
    'publication_stats',
    'analytics'
    ]

test_requires = []

setup(
    name="analytics",
    version='0.0.4',
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
        "Operating System :: POSIX :: Linux",
        "Topic :: System",
        "Topic :: Services",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    dependency_links=[
        "git+https://github.com/scieloorg/xylose@v0.32#egg=xylose",
        "git+https://github.com/scieloorg/thriftpy-wrap@0.1.1#egg=thriftpywrap",
        "git+https://github.com/scieloorg/access_stats@0.1.2#egg=publication_stats",
        "git+https://github.com/scieloorg/analytics@0.0.4#egg=analytics"
    ],
    message_extractors = {
        'analytics': [
            ('**.py', 'python', None),
            ('templates/**.html', 'mako', None),
            ('templates/**.mako', 'mako', None),
            ('static/**', 'ignore', None)
        ]
    },
    include_package_data=True,
    zip_safe=False,
    setup_requires=["nose>=1.0", "coverage"],
    tests_require=test_requires,
    install_requires=install_requires,
    test_suite="nose.collector",
    entry_points="""\
    [paste.app_factory]
    main = analytics:main
    """,
)