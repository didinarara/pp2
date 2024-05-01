import psycopg2


conn = psycopg2.connect(
    host='localhost',
    dbname='suppliers',
    user='postgres',
    password='motfootball23'
)

cur = conn.cursor()

cur.execute('DROP TABLE phonebook;')

conn.commit()


cur.execute("""CREATE TABLE phonebook (
    name VARCHAR(255),
    username VARCHAR(255),
    phone_number VARCHAR(20)
);
""")

conn.commit()



import csv


def upload_from_csv(file_path):
    connection = psycopg2.connect(user="postgres",
                                  password="motfootball23",
                                  host="localhost",
                                  port="5432",
                                  database="suppliers")
    cursor = connection.cursor()
    
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            name, username, phone_number = row
            cursor.execute("INSERT INTO phonebook (name, username, phone_number) VALUES (%s, %s, %s)", (name, username, phone_number))
            connection.commit()
    
    cursor.close()
    connection.close()

# Function to insert data from console
def insert_from_console():
    name = input("Enter name: ")
    username = input("Enter username: ")
    phone_number = input("Enter phone number: ")

    connection = psycopg2.connect(user="postgres",
                                  password="motfootball23",
                                  host="localhost",
                                  port="5432",
                                  database="suppliers")
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO phonebook (name, username, phone_number) VALUES (%s, %s, %s)", (name, username, phone_number))
    connection.commit()
    
    cursor.close()
    connection.close()
    
    
# Example usage
if __name__ == "__main__":
    # Upload data from CSV
    upload_from_csv('contacts.csv')

    # Insert from console
    insert_from_console()
    
    
# Function to update data
def update_number(student_id, new_number):
    conn = psycopg2.connect(user="postgres",
                            password="motfootball23",
                            host="localhost",
                            port="5432",
                            database="suppliers")
    
    cur = conn.cursor()

    cur.execute("""UPDATE phonebook
        SET phone_number = %s
        WHERE name = %s;
    """, (new_number, student_id))

    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()

# Example usage
update_number('Zhanel', 4753274)



# Deleting data
cur.execute("""DELETE FROM phonebook
            WHERE name = 'Aisha'; 
""")

conn.commit()