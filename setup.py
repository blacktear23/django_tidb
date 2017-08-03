#!/usr/bin/env python

from distutils.core import setup

long_description = """TiDB backend for Django"""

setup(
    name='django_tidb',
    version='1.0',
    author='Rain Li',
    author_email='blacktear23@gmail.com',
    url='http://github.com/blacktear23/django_tidb',
    download_url='http://github.com/blackear23/django_tidb/archive/1.0.tar.gz',
    description='TiDB backend for Django',
    long_description=long_description,
    keywords=['django', 'tidb'],
    packages=['django_tidb', 'django_tidb.tidb'],
    license='Apache2',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries',
    ],
)
