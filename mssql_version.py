from mssql_connection import get_cursor


cursor = get_cursor()

cursor.execute("SELECT @@version;")
result = cursor.fetchone()
print(result[0])
