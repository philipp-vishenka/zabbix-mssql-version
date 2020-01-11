import mssql_connection


cursor = mssql_connection.get_cursor()

cursor.execute("SELECT @@version;")
row = cursor.fetchone()
print(row[0])
