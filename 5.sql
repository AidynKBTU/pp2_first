import psycopg2

conn = psycopg2.connect(
    dbname="your_dbname",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)
cur = conn.cursor()

def delete_data():
    user_id = input("Enter User ID to delete: ")
    cur.execute("DELETE FROM contacts WHERE user_id = %s", (user_id,))
    cur.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
    conn.commit()
    print("Data deleted successfully!")

delete_data()

# Close connection
cur.close()
conn.close()
