import psycopg2

def search_records(pattern):
    conn = psycopg2.connect(
        host='localhost',
        dbname='suppliers',
        user='postgres',
        password='motfootball23'
    )
    cur = conn.cursor()

    # Search for records based on the pattern in name, username, or phone_number columns
    cur.execute("""
        SELECT * FROM phonebook
        WHERE name LIKE %s OR username LIKE %s OR phone_number LIKE %s;
    """, ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))

    records = cur.fetchall()

    cur.close()
    conn.close()

    return records

# Example usage:
pattern = input("Enter pattern (name, username, or phone number): ")
records = search_records(pattern)
for record in records:
    print(record)
