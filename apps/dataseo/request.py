import requests
import logging
import traceback
import ssl
import socket
from json import JSONDecodeError
from requests.auth import HTTPBasicAuth
from requests import exceptions

from apps.config import DATAFORSEO_CREDENTIALS, DATAFORSEO_URL

logger = logging.getLogger(__name__)


def request(keyword, **kwargs):
	filters = {key: value for key, value in kwargs.items() if value}
	data = {'keyword': keyword, **filters}

	attrs = {
		'json': [data],
		'auth': HTTPBasicAuth(*DATAFORSEO_CREDENTIALS),
		'timeout': 60
	}
	try:
		response = requests.request("POST", DATAFORSEO_URL, **attrs)
		if response.status_code == 200:
			return response.json()
	except exceptions.ConnectionError:
		logger.exception("ConnectionError occured")
	except exceptions.Timeout:
		logger.exception("TimeoutError occured")
	except ssl.SSLError:
		logger.exception("SSLError occured")
	except socket.timeout:
		logger.exception("Socket TimeoutError occured")
	except JSONDecodeError as exp:
		logger.exception(f"DATAFORSEO server API response data is not JSON decodable.\n data: {response.text}\nTraceback: {traceback.format_exc()}")
	except Exception as exp:
		logger.exception("Error occured while connecting to DATAFORSEO server.\nReason:{exp}\nTraceback: {traceback.format_exc()}")

	return None
