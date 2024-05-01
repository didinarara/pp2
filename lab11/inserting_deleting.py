import psycopg2
import csv

def create_table():
    conn = psycopg2.connect(
        host='localhost',
        dbname='suppliers',
        user='postgres',
        password='motfootball23'
    )
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS phonebook;')
    cur.execute("""CREATE TABLE phonebook (
        name VARCHAR(255),
        username VARCHAR(255) PRIMARY KEY,
        phone_number VARCHAR(20)
    );""")
    conn.commit()
    cur.close()
    conn.close()

def upload_from_csv(file_path):
    conn = psycopg2.connect(
        host='localhost',
        dbname='suppliers',
        user='postgres',
        password='motfootball23'
    )
    cur = conn.cursor()
    
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            name, username, phone_number = row
            cur.execute("INSERT INTO phonebook (name, username, phone_number) VALUES (%s, %s, %s)", (name, username, phone_number))
            conn.commit()
    
    cur.close()
    conn.close()

def insert_or_update_user(name, username, phone_number):
    conn = psycopg2.connect(
        host='localhost',
        dbname='suppliers',
        user='postgres',
        password='motfootball23'
    )
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
    existing_record = cur.fetchone()

    if existing_record:
        cur.execute("UPDATE phonebook SET phone_number = %s, username = %s WHERE name = %s", (phone_number, username, name))
    else:
        cur.execute("INSERT INTO phonebook (name, username, phone_number) VALUES (%s, %s, %s)", (name, username, phone_number))

    conn.commit()

    cur.close()
    conn.close()


def delete_by_username_or_phone(username_or_phone):
    conn = psycopg2.connect(
        host='localhost',
        dbname='suppliers',
        user='postgres',
        password='motfootball23'
    )
    cur = conn.cursor()

    cur.execute("DELETE FROM phonebook WHERE username = %s OR phone_number = %s", (username_or_phone, username_or_phone))
    conn.commit()

    cur.close()
    conn.close()


# Create table
create_table()

# Upload data from CSV
upload_from_csv('contacts.csv')

# Example usage for inserting or updating user
name = input("Enter name: ")
username = input("Enter username: ")
phone_number = input("Enter phone number: ")
insert_or_update_user(name, username, phone_number)

# Example usage for deleting data
username_or_phone = input("Enter username or phone number to delete: ")
delete_by_username_or_phone(username_or_phone)
