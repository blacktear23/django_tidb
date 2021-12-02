#from django.db.backends.mysql import schema as myschema


#class DatabaseSchemaEditor(myschema.DatabaseSchemaEditor):
#    sql_delete_table = "DROP TABLE %(table)s"
#    sql_delete_column = "ALTER TABLE %(table)s DROP COLUMN %(column)s"
#
#    def remove_field(self, model, field):
        # Drop any Index, TiDB requires explicite deletion
#        if field.db_index:
#            idx_names = self._constraint_names(model, [field.column], index=True)
#            for idx_name in idx_names:
#                self.execute(self._delete_constraint_sql(self.sql_delete_index, model, idx_name))
#        super(DatabaseSchemaEditor, self).remove_field(model, field)
#

from django.db.backends.mysql.schema import (
    DatabaseSchemaEditor as MysqlDatabaseSchemaEditor,
)


class DatabaseSchemaEditor(MysqlDatabaseSchemaEditor):
    @property
    def sql_delete_check(self):
        return 'ALTER TABLE %(table)s DROP CHECK %(name)s'

    @property
    def sql_rename_column(self):
        return 'ALTER TABLE %(table)s CHANGE %(old_column)s %(new_column)s %(type)s'

    def skip_default_on_alter(self, field):
        return False

    @property
    def _supports_limited_data_type_defaults(self):
        return True

    def _field_should_be_indexed(self, model, field):
        return False
 
