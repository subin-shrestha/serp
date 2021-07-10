from google.api_core import exceptions
from google.cloud import bigquery


class Dataset:
    def __init__(self, client):
        self.client = client

    def get_or_create_dataset(self, dataset_name, location='US'):
        qualified_dataset = f"{self.client.project}.{dataset_name}"
        try:
            dataset = self.client.get_dataset(qualified_dataset)
            return dataset, False
        except exceptions.NotFound:

            # build project.dataset_name
            dataset = bigquery.Dataset(qualified_dataset)
            dataset.location = location

            try:
                dataset = self.client.create_dataset(dataset)  # Make an API request.
            except exceptions.Conflict:
                raise exceptions.Conflict(f"Dataset with name {dataset_name} already exists.")

        return dataset, True
