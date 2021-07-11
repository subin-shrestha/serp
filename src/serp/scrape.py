import uuid
import argparse
from apps.dataseo import request
from apps.bq import BigQuery


bq = BigQuery()

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
	response = request(keyword=keyword, device=device, location_code=location_code, language_code=language_code)

	if response:
		try:
			result = response['tasks'][0]['result'][0]
		except (IndexError, KeyError):
			print("No results found.")

		items = result.get('items') or []
		results = []

		for item in items[:10]:
			results.append({
				'id': uuid.uuid4().hex,
				'type': item.get('type', ""),
				'rank_group': item.get('rank_group', 0),
				'rank_absolute': item.get('rank_absolute', 0),
				'position': item.get('position', ""),
				'xpath': item.get('xpath'),
				'url': item.get('url'),
				'title': item.get('title'),
				'breadcrumb': item.get('breadcrumb'),
				'is_image': item.get('is_image'),
				'is_video': item.get('is_video'),
				'is_featured_snippet': item.get('is_featured_snippet'),
				'is_malicious': item.get('is_malicious'),
				'is_web_story': item.get('is_web_story'),
			})

		if results:
			bq.init_table("result")
			bq.insert(results)



