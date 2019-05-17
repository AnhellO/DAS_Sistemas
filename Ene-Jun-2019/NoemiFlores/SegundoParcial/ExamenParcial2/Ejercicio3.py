import sqlite3

con = sqlite3.connect('datUsers.db')
cursor = con.cursor()

cursor.execute('''
    CREATE TABLE Users(
    Gender TEXT NOT NULL,
    First TEXT NOT NULL,
    Last TEXT NOT NULL,
    Location TEXT NOT NULL,
    Email TEXT NOT NULL)
    ''')

con.close()