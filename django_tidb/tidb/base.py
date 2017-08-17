"""
TiDB database backend for Django. Based on django's MySQL backend

Requires mysqlclient: https://pypi.python.org/pypi/mysqlclient/
MySQLdb is supported for Python 2 only: http://sourceforge.net/projects/mysql-python
"""

from django.db.backends.mysql import base as mybase

# Some of these import MySQLdb, so import them after checking if it's installed.
from .features import DatabaseFeatures                      # isort:skip
from .schema import DatabaseSchemaEditor                    # isort:skip


class DatabaseWrapper(mybase.DatabaseWrapper):
    SchemaEditorClass = DatabaseSchemaEditor

    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)
        self.features = DatabaseFeatures(self)
