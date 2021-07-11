from google.cloud import bigquery

SCHEMAS = {
	# 'search': [
	# 	bigquery.SchemaField("id", "STRING", "REQUIRED"),
	# 	bigquery.SchemaField("datetime", "DATETIME", "REQUIRED"),
	# 	bigquery.SchemaField("keyword", "STRING", "REQUIRED"),
	# 	bigquery.SchemaField("type", "STRING",),
	# 	bigquery.SchemaField("location_code", "INTEGER", "REQUIRED"),
	# 	bigquery.SchemaField("language_code", "STRING", "REQUIRED"),
	# 	bigquery.SchemaField("check_url", "STRING", "REQUIRED"),
	# 	bigquery.SchemaField("items_count", "INTEGER"),
	# ],

	'result': [
		bigquery.SchemaField("id", "STRING", "REQUIRED"),
		bigquery.SchemaField("type", "STRING", "REQUIRED"),
		bigquery.SchemaField("rank_group", "INTEGER", "REQUIRED"),
		bigquery.SchemaField("rank_absolute", "INTEGER", "REQUIRED"),
		bigquery.SchemaField("position", "STRING", "REQUIRED"),
		bigquery.SchemaField("xpath", "STRING"),
		bigquery.SchemaField("url", "STRING"),
		bigquery.SchemaField("title", "STRING"),
		bigquery.SchemaField("breadcrumb", "STRING"),
		bigquery.SchemaField("description", "STRING"),
		bigquery.SchemaField("is_image", "BOOLEAN"),
		bigquery.SchemaField("is_video", "BOOLEAN"),
		bigquery.SchemaField("is_featured_snippet", "BOOLEAN"),
		bigquery.SchemaField("is_malicious", "BOOLEAN"),
		bigquery.SchemaField("is_web_story", "BOOLEAN"),
		# bigquery.SchemaField("text", "STRUCT"),
		# bigquery.SchemaField("links", "STRUCT"),
		# bigquery.SchemaField("items", "STRUCT"),
	]
}