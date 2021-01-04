import psycopg2

from config import postgres

class database:


	def __init__(self):
		self.dbname = postgres['dbname']
		self.user = postgres['user']
		self.password = postgres['password']


	def excute_commands(self, sql):
		try:
			conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password)
			cur = conn.cursor()
			for command in sql:
				if command:
					cur.execute(command)
			conn.commit()
			cur.close()
			conn.close()
		except Exception as error:
			print('error on executing command to db:\n')
			print(error)
			return False
		return True


	def insert_data(self, table, columns, data):

		sql = "INSERT INTO " + table +  "(" + ",".join(columns) + ") VALUES (" + ",".join(["%s"] * len(columns)) + ");";

		try:
			conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password)
			cur = conn.cursor() 
			for row in data:
				cur.execute(sql, [row[column] for column in columns])
			conn.commit()
			cur.close()
			conn.close()
		except Exception as error:
			print('error on storing data to db:\n')
			print(error)
			return False
		return True