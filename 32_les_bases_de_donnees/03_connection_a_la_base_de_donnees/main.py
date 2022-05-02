import sqlite3

connection = sqlite3.connect('test.db')
print('Connecté!')
connection.close()