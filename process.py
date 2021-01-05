from database import *
from input_file import *


class process:


	def run_sql_from_file(self, file):
		in_file = input_file(file)
		commands = in_file.get_content()
		db = database()
		res = db.excute_commands(commands.split(';'))
		if res:
			print(file + " commands executed successfully")
			return True
		return False


	def load_data_from_json_file_to_db(self, file, table, columns, filter_date = ''):
		data = self.load_json_data_from_file(file, filter_date)
		return self.store_data(table, columns, data)		


	def load_json_data_from_file(self, file, filter_date = ''):
		in_file = input_file(file)
		return in_file.get_json()


	def store_data(self, table, columns, data):
		db = database()
		res = db.insert_data(table, columns, data)
		if res:			
			print("data loaded successfully to table " + table)			
			return True
		return False
