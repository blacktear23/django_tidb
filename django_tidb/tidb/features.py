from django.db.backends.mysql import base as mybase


class DatabaseFeatures(mybase.DatabaseFeatures):
    supports_foreign_keys = False
    uses_savepoints = False
    has_select_for_update = True
    supports_transactions = False
    uses_savepoints = False
    can_release_savepoints = False
    atomic_transactions = False
    supports_atomic_references_rename = False
    can_clone_databases = False
    can_rollback_ddl = False
    order_by_nulls_first = True
    supports_foreign_keys = False
    indexes_foreign_keys = False
