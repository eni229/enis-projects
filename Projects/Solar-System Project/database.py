import sqlite3, os


#connecting to database
class Connect:
	def __init__ (self, database): #initialise values
		self.database = database

	def connect(self): #for checking if connecting
		conn = sqlite3.connect(self.database)
		return conn
		conn.close()

	def getValues(self, num, field): #get values from the database 
		conn = sqlite3.connect(self.database)
		mycursor = conn.cursor() #connects to the database

		values = 'Select ' + field +' from Planets where id = ' + str(num) #testing retrieving values 
		mycursor.execute(values)
		myresult =  mycursor.fetchone()[0] #this gets the actual value from the array
		return myresult #returns the value
		conn.close()
		mycursor.close()



class File: #for load button
	def __init__(self, filename):
		self.filename = filename #intialise variables

	def validate(self): #checks if correct file
		if self.filename.endswith('.db'): #checks if database file
			directory, dbname = os.path.split(self.filename) #splits path from directory

			return True #valid file
		else:
			return False #invalid file


'''
	def saveValues(self, num, field, value):
		conn = sqlite3.connect(self.database)
		mycursor = conn.cursor() #connects to the database

		values = 'Update Planets set ' + field + '=' + str(value) + ' where id = ' + str(num) #sql statement
		mycursor.execute(values)

		mycursor.close()
		conn.close() '''