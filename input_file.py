import json

class input_file:

	def __init__(self, path):
		self.input_path = path
		self.content = self.read_file()


	def read_file(self):
		try:
			f = open(self.input_path, "r")
			content = f.read() # in this case we know we have small files that fit in memory
			f.close()	
		except Exception as error:
			print('error on reading input file:\n')
			print(error)
			return False
		return content


	def get_content(self):		
		return self.content		


	def get_json(self):
		try:
			js = json.loads(self.content)
		except ValueError as error:
			print('error on loading content to json:\n')
			print(error)
			return False
		return js