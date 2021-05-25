from django.db.backends.mysql import base as mybase
from django.utils.functional import cached_property


class DatabaseFeatures(mybase.DatabaseFeatures):
    supports_foreign_keys = False
    uses_savepoints = False

    @cached_property
    def can_introspect_foreign_keys(self):
        return False
