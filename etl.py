from config import input_data
from process import *


start_date = datetime.strptime(input_data['min_date'], '%Y-%m-%d').date()
end_date = datetime.strptime(input_data['max_date'], '%Y-%m-%d').date()

etl = process()



tables_created = etl.run_sql_from_file('create_tables.sql')

if tables_created:

	orgs_loaded = etl.load_data_from_json_file_to_db(
			input_data['data_dir'] + input_data['orgs_file'],
			"load.organization",
			['organization_key', 'organization_name', 'created_at']
		)

	# iterate over days	
	for single_date in etl.daterange(start_date, end_date):
		events_loaded = etl.load_data_from_json_file_to_db(
				input_data['data_dir'] + input_data['events_file'],
				"load.event",
				['id', 'event_type', 'username', 'user_email', 'user_type', 'organization_name', 'plan_name', 'received_at'],
				single_date
			)

		events_loaded *= events_loaded

	if orgs_loaded and events_loaded:

		res = etl.run_sql_from_file('transform_data.sql')