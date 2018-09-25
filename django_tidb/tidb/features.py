from django.db.backends.mysql import base as mybase


class DatabaseFeatures(mybase.DatabaseFeatures):
    supports_foreign_keys = False
    uses_savepoints = False
