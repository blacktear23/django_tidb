from django.db.backends.mysql import schema as myschema


class DatabaseSchemaEditor(myschema.DatabaseSchemaEditor):
    sql_delete_table = "DROP TABLE %(table)s"
    sql_delete_column = "ALTER TABLE %(table)s DROP COLUMN %(column)s"

    def remove_field(self, model, field):
        # Drop any Index, TiDB requires explicite deletion
        if field.db_index:
            idx_names = self._constraint_names(model, [field.column], index=True)
            for idx_name in idx_names:
                self.execute(self._delete_constraint_sql(self.sql_delete_index, model, idx_name))
        super(DatabaseSchemaEditor, self).remove_field(model, field)
