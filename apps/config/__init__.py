import os, sys

BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)

BQ_GCP_PROJECT_ID = ""
GCP_SERVICE_ACCOUNT_CREDENTIALS = BASE_DIR + "/credentials.json"

DATAFORSEO_URL = ""
DATAFORSEO_CREDENTIALS = ["", ""]

try:
	from .credentials import *
except ImportError:
	pass
