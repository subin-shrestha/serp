from google.cloud import bigquery
from google.oauth2.service_account import Credentials
from apps.config import BQ_GCP_PROJECT_ID, GCP_SERVICE_ACCOUNT_CREDENTIALS

from .dataset import Dataset
from .table import Table
from .schema import SCHEMAS


class BigQuery:
	project = BQ_GCP_PROJECT_ID
	dataset_name = "test_serp"
	big_table = None

	def __init__(self):
		self.credentials = Credentials.from_service_account_file(GCP_SERVICE_ACCOUNT_CREDENTIALS)
		self.client = bigquery.Client(project=self.project, credentials=self.credentials)

		self.dataset = Dataset(self.client)
		self.table = Table(self.client)

	def init_table(self, table_id):
		''' Get or Create Job table.'''

		schema = SCHEMAS.get(table_id)
		self.big_dataset, _ = self.dataset.get_or_create_dataset(self.dataset_name)
		self.big_table, _ = self.table.get_or_create_table(self.dataset_name, table_id, schema)

	def insert(self, row_data):
		if row_data:
			for r in range(0, len(row_data), 1000):
				start = r
				end = r + 1000
				status = self.client.insert_rows(self.big_table, rows=row_data[start:end])
				if status:
					print(row_data)
					print(status)

	def delete(self, id):
		exists_query = (
			f"DELETE FROM "
			f"{self.big_table.project}.{self.big_table.dataset_id}.{self.big_table.table_id} "
			f"WHERE id = @id ")

		job_config = bigquery.QueryJobConfig(query_parameters=[
			bigquery.ScalarQueryParameter("id", "STRING", id),
		])

		return self._query_job(exists_query, job_config)

	def _query_job(self, query, job_config=None):
		if not job_config:
			job_config = bigquery.QueryJobConfig()

		job_config.use_query_cache = True
		job_config.use_legacy_sql = False

		query_job = self.client.query(query=query, job_config=job_config)
		result = query_job.result()
		return bool(result.total_rows)
