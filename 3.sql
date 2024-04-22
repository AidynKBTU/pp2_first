import psycopg2

conn = psycopg2.connect(
    dbname="your_dbname",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)
cur = conn.cursor()

def update_data():
    user_id = input("Enter User ID: ")
    new_first_name = input("Enter New First Name (Press Enter to skip): ")
    new_phone_number = input("Enter New Phone Number (Press Enter to skip): ")

    if new_first_name:
        cur.execute("UPDATE users SET first_name = %s WHERE user_id = %s", (new_first_name, user_id))
        conn.commit()
    if new_phone_number:
        cur.execute("UPDATE contacts SET phone_number = %s WHERE user_id = %s", (new_phone_number, user_id))
        conn.commit()

update_data()

# Close connection
cur.close()
conn.close()
