import sqlite3

# Connect to the database file
conn = sqlite3.connect('db.sqlite3')

# Create a cursor object
cursor = conn.cursor()

# Define the table name
table_name = 'personalized_index_personalizedindexstock'

# Delete all records from the table and reset the auto increment value of primary key
cursor.execute(f"DELETE FROM {table_name}")

# Commit the changes
conn.commit()

# Close the connection
conn.close()
