from google.api_core import exceptions
from google.cloud import bigquery


class Table:
    def __init__(self, client):
        self.client = client

    def get_or_create_table(self, dataset_id, table_id, schema, location='US'):
        qualified_table = f"{self.client.project}.{dataset_id}.{table_id}"

        try:
            table = self.client.get_table(qualified_table)
            return table, False
        except exceptions.NotFound:
            try:
                table_data = bigquery.Table(qualified_table, schema=schema)
                table_result = self.client.create_table(table_data)
                table = self.client.get_table(qualified_table)
            except exceptions.Conflict:
                raise exceptions.Conflict(
                    f"Table with name {table_id} already exists.")

        return table, True

    def delete_table(self, table_id):
        try:
            self.client.delete_table(table_id, not_found_ok=True)
            return True
        except Exception as e:
            print(f"Failed to delete table {table_id}. {str(e)}")
            return False
