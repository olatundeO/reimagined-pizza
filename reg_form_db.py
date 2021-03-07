import sqlite3

conn = sqlite3.connect('reg_form.db')
cursor = conn.cursor()


cursor.execute('CREATE TABLE Student (student (Lastname TEXT, Firstname TEXT, Email TEXT, Gender TEXT, '
               'Qualification TEXT, Personal Statement TEXT) primary key)')

cursor.execute(('INSERT INTO Student (Lastname, Firstname, Email, Gender, Qualification, Personal Statement) VALUES (?,?,?,?,?,?)'))

conn.commit()
