import psycopg2

conn = psycopg2.connect(
    dbname="your_dbname",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)
cur = conn.cursor()

def query_data():
    user_id = input("Enter User ID (Press Enter to skip): ")
    if user_id:
        cur.execute(
            "SELECT * FROM users JOIN contacts ON users.user_id = contacts.user_id WHERE users.user_id = %s",
            (user_id,)
        )
    else:
        cur.execute("SELECT * FROM users JOIN contacts ON users.user_id = contacts.user_id")
    
    rows = cur.fetchall()
    for row in rows:
        print(row)

query_data()

# Close connection
cur.close()
conn.close()
