import psycopg2
import pandas as pd
# Connection parameters
db_host = 'postgres:5432'
db_name = 'food_db'
db_user = 'myuser'
db_password = 'mypassword'
# CSV file path
csv_file = 'food_database.csv'
# Create a connection to PostgreSQL
conn = psycopg2.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_password
)
# Create a cursor object
cursor = conn.cursor()
# Create table query
create_table_query = """
CREATE TABLE IF NOT EXISTS food_info (
    label VARCHAR(255),
    calories INT,
    protein INT,
    carbohydrates INT,
    fats INT,
    fiber INT,
    sugars INT,
    sodium INT
);
"""
# Execute the query to create the table
cursor.execute(create_table_query)
conn.commit()
# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)
# Insert data into the database
for index, row in df.iterrows():
    insert_query = """
    INSERT INTO food_info (label, calories, protein, carbohydrates, fats, fiber, sugars, sodium)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    cursor.execute(insert_query, tuple(row))
# Commit the changes
conn.commit()
# Close the cursor and connection
cursor.close()
conn.close()
print("Data inserted successfully.")