from datetime import *

from database import *
from input_file import *


class process:


	def run_sql_from_file(self, file):
		in_file = input_file(file)
		commands = in_file.get_content()
		#print(commands.split(';'))
		db = database()
		res = db.excute_commands(commands.split(';'))
		if res:
			print(file + " commands executed successfully")
			return True
		return False


	def load_data_from_json_file_to_db(self, file, table, columns, filter_date = ''):
		in_file = input_file(file)
		data = in_file.get_json()
		data = self.filter_data(filter_date, data) if filter_date else data
		db = database()
		res = db.insert_data(table, columns, data)
		if res:
			if filter_date:
				print(file + " data loaded successfully to table " + table + " for date " + str(filter_date))
			else:
				print(file + " data loaded successfully to table " + table)
			return True
		return False


	def filter_data(self, filter_date, data):
		new_data = list()
		for row in data:
			# assume that we have "standard" column name ('received_at') in all files to filter our data to simplify the process
			received_at_obj = datetime.strptime(row['received_at'], '%Y-%m-%d %H:%M:%S.%f')
			if received_at_obj.date() == filter_date:
				new_data.append(row)		
		return new_data


	def daterange(self, start_date, end_date):
		for n in range(int((end_date - start_date).days)):
			yield start_date + timedelta(n)




