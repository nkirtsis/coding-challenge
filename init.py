from config import input_data
from process import *


process = process()


tables_created = process.run_sql_from_file('create_tables.sql')

if tables_created:

	orgs_loaded = process.load_data_from_json_file_to_db(
			input_data['data_dir'] + input_data['orgs_file'],
			"load.organization",
			['organization_key', 'organization_name', 'created_at']
		)
