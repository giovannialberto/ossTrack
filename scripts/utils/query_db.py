import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data/github_metrics.db')

# Query the table content
df = pd.read_sql_query("SELECT * from metrics", conn)
print(df.head())

# Get the column names
columns = list(df.columns)

# Close the database connection
conn.close()