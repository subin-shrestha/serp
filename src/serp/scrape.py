import argparse
from apps.dataseo import request


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-k", "--keyword", type=str, required=True)
	parser.add_argument("-loc", "--location", type=int)
	parser.add_argument("-lang", "--language", type=str, default="en")
	parser.add_argument("-d", "--device", type=str, choices=['desktop', 'mobile'])

	args = parser.parse_args()
	keyword = args.keyword
	device = args.device
	location_code = args.location
	language_code = args.language
	request(keyword=keyword, device=device, location_code=location_code, language_code=language_code)
