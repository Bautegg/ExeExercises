import psycopg2
# Connect to your postgres DB
con_creds = "postgresql://postgres:Alfaomega15!@localhost:5432/dvdrental"

conn = psycopg2.connect(con_creds)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
first_querry = """
SELECT last_name 
FROM customer 
LIMIT 20
"""

cur.execute(first_querry)

# Retrieve query results
records = cur.fetchall()

print(records)
for i in records:
    print(i)

conn.close()