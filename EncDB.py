from pysqlcipher3 import dbapi2 as sqlcipher
from secrets import key
import os
import pandas as pd

class EncryptDB:

	def __init__(self):
		self.pt_connect=sqlcipher.connect('Balance.db')

	def createDB(self, data):
		df=pd.DataFrame(data)
		df.to_sql(name='BalanceTable', con=self.pt_connect, if_exists='replace', index=False)

	def readPT(self): #Read Plain Text Data from Unencrypted DB
		c=self.pt_connect.execute('select * from BalanceTable;')
		data=c.fetchall()
		print(data)
		c.close()

	def encrypt(self): #Encrypt an Existing Database and Destroy the Original
		cur=self.pt_connect.cursor()
		cur.execute('ATTACH DATABASE "encrypted.db" AS encrypted KEY {};'.format(key))
		cur.execute("SELECT sqlcipher_export('encrypted');")
		cur.execute('DETACH DATABASE encrypted;')
		self.pt_connect.commit()
		cur.close()
		os.remove('Balance.db')

	def readEncrypted(self): #Read Encrypted Database
		self.enc=sqlcipher.connect('encrypted.db')
		self.enc.execute('pragma key={}'.format(key))
		print(self.enc.execute('select * from BalanceTable;').fetchall())

def main():
	data={
	'First Name':['Eliot','Darlene','Angela','Ollie','Tyrell','Dominque','Phillip','Krista','Gideon','Terry'],
	'Last Name':['Alderson','Alderson','Moss','Parker','Wellick','DiPierro','Price','Gordon','Goddard','Colby'],
	'Balance':[1000,2000,3000,3500,2200,3250,4000,2300,5000,1500]
		}

	E=EncryptDB()
	E.readEncrypted()

if __name__=='__main__':
	main()


from pysqlcipher3 import dbapi2 as sqlcipher
from secrets import key
import os
import pandas as pd

class EncryptDB:

	def __init__(self):
		self.pt_connect=sqlcipher.connect('Balance.db')

	def createDB(self, data):
		df=pd.DataFrame(data)
		df.to_sql(name='BalanceTable', con=self.pt_connect, if_exists='replace', index=False)

	def readPT(self): #Read Plain Text Data from Unencrypted DB
		c=self.pt_connect.execute('select * from BalanceTable;')
		data=c.fetchall()
		print(data)
		c.close()

	def encrypt(self): #Encrypt an Existing Database and Destroy the Original
		cur=self.pt_connect.cursor()
		cur.execute('ATTACH DATABASE "encrypted.db" AS encrypted KEY {};'.format(key))
		cur.execute("SELECT sqlcipher_export('encrypted');")
		cur.execute('DETACH DATABASE encrypted;')
		self.pt_connect.commit()
		cur.close()
		os.remove('Balance.db')

	def readEncrypted(self): #Read Encrypted Database
		self.enc=sqlcipher.connect('encrypted.db')
		self.enc.execute('pragma key={}'.format(key))
		print(self.enc.execute('select * from BalanceTable;').fetchall())

def main():
	data={
	'First Name':['Eliot','Darlene','Angela','Ollie','Tyrell','Dominque','Phillip','Krista','Gideon','Terry'],
	'Last Name':['Alderson','Alderson','Moss','Parker','Wellick','DiPierro','Price','Gordon','Goddard','Colby'],
	'Balance':[1000,2000,3000,3500,2200,3250,4000,2300,5000,1500]
		}

	E=EncryptDB()
	E.readEncrypted()

if __name__=='__main__':
	main()





	
