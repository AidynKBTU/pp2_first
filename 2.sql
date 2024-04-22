import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="your_dbname",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)
cur = conn.cursor()

# Function to insert data from console
def insert_data():
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    phone_number = input("Enter Phone Number: ")
    
    cur.execute(
        "INSERT INTO users (first_name, last_name) VALUES (%s, %s) RETURNING user_id",
        (first_name, last_name)
    )
    user_id = cur.fetchone()[0]
    cur.execute(
        "INSERT INTO contacts (user_id, phone_number) VALUES (%s, %s)",
        (user_id, phone_number)
    )
    conn.commit()
    print("Data inserted successfully!")

insert_data()

# Close connection
cur.close()
conn.close()