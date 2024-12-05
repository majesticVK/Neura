import sqlite3

conn=sqlite3.connect("Neura.db")
cursor=conn.cursor()
query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO sys_command VALUES (null,'ONENOTE', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE')"
cursor.execute(query)
conn.commit()

query = "INSERT INTO sys_command VALUES (null,'Blender 4.2', 'C:\\Program Files\\Blender Foundation\\Blender 4.2')"
cursor.execute(query)
conn.commit()


query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
cursor.execute(query)
conn.commit()
