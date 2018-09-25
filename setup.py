#!/usr/bin/env python

from distutils.core import setup

long_description = """TiDB backend for Django"""

setup(
    name='django_tidb',
    version='2.1.1',
    author='Rain Li',
    author_email='blacktear23@gmail.com',
    url='http://github.com/blacktear23/django_tidb',
    download_url='http://github.com/blackear23/django_tidb/archive/2.1.tar.gz',
    description='TiDB backend for Django',
    long_description=long_description,
    keywords=['django', 'tidb'],
    packages=['django_tidb', 'django_tidb.tidb'],
    license='Apache2',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries',
    ],
)
