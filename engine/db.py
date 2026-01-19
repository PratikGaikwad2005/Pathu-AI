import sqlite3

conn = sqlite3.connect('pathuDB.db')

cursor = conn.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# to insert values
# query = "INSERT INTO sys_command VALUES (null,'Command Prompt', 'C:\\WINDOWS\\system32\\cmd.exe')"
# cursor.execute(query)
# conn.commit()
# conn.close()  # Don't forget to close the connection when done

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# to insert values
# query = "INSERT INTO web_command VALUES (null,'Linkdin', 'https://www.linkedin.com')"
# cursor.execute(query)
# conn.commit()
# conn.close()  # Don't forget to close the connection when done


# To fetch values from sys_command tables
query = "Command Prompt"
cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (query,))
results = cursor.fetchall()
print(results[0][0])