import unittest

from config import test_data
from database import *
from input_file import *

class TestInputFile(unittest.TestCase):

	def test_wrong_file_path(self):
		"""
        should return False cause file path does not exist
        """
		in_file = input_file('foo' + test_data['input_file'])
		content = in_file.get_content()
		self.assertFalse(content)

	def test_read_file_content(self):
		"""
        should read content from file
        """
		in_file = input_file(test_data['data_dir'] + test_data['input_file'])
		content = in_file.get_content()
		self.assertEqual(content, "lorem ipsum")

	def test_read_json_content(self):
		"""
        should read json content from file
        """
		in_file = input_file(test_data['data_dir'] + test_data['input_json'])
		json = in_file.get_json()
		print(json)
		self.assertEqual(json[0]['lorem'], "ipsum")


class TestDatabase(unittest.TestCase):
	
	def test_wrong_command(self):
		"""
		should return False cause syntax error
		"""        
		db = database()
		commands = "SELE"
		res = db.excute_commands(commands.split(';'))		
		self.assertFalse(res)

	def test_one_command(self):
		"""
		should return True cause command is fine
		"""        
		db = database()
		commands = "SELECT 1"
		res = db.excute_commands(commands.split(';'))		
		self.assertTrue(res)

	def test_multiple_commands(self):
		"""
		should return True cause commands are fine
		"""        
		db = database()
		commands = "SELECT 1;SELECT 2;SELECT 3"
		res = db.excute_commands(commands.split(';'))		
		self.assertTrue(res)

	def test_wrong_table_insert(self):
		"""
		should return False cause table does not exist
		"""        
		db = database()
		table = "foo"
		columns = ["id", "name"]
		data = [{'id': '1', 'name': 'foobar'}, {'id': '2', 'name': 'barfoo'}]
		res = db.insert_data(table, columns, data)		
		self.assertFalse(res)

	def test_wrong_column_insert(self):
		"""
		should return False cause column does not exist
		"""        
		db = database()
		table = "test.test"
		columns = ["source_id", "name"]
		data = [{'id': '1', 'name': 'foobar'}, {'id': '2', 'name': 'barfoo'}]
		res = db.insert_data(table, columns, data)		
		self.assertFalse(res)

	def test_no_data_insert(self):
		"""
		should return True cause no data is fine
		"""        
		db = database()
		table = "test.test"
		columns = ["id", "name"]
		data = []
		res = db.insert_data(table, columns, data)		
		self.assertTrue(res)

	def test_table_insert(self):
		"""
		should return True cause insert works fine
		"""        
		db = database()
		table = "test.test"
		columns = ["id", "name"]
		data = [{'id': '1', 'name': 'foobar'}, {'id': '2', 'name': 'barfoo'}]
		res = db.insert_data(table, columns, data)		
		self.assertTrue(res)



if __name__ == '__main__':
	unittest.main()