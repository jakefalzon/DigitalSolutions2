import sqlite3

conn = sqlite3.connect("Company.db")

conn.execute('''DROP TABLE IF EXISTS CUSTOMERS; ''')

conn.execute('''CREATE TABLE CUSTOMERS
            (ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            AGE INT,
            DOB DATE NOT NULL,
            POSTCODE INT NOT NULL);''')

myTuple = """INSERT INTO CUSTOMERS (id, name, age, DOB, postcode) VALUES (?,?,?,?,?)""";

records_to_insert = [[2, 'Flynn', 29, '2016-1-1', 4099],
[3, 'Flynnv2', 45, '2016-2-2', 2069],
[4, 'Flynnv3', 99, '2016-3-3', 8888],
[5, 'Flynnv4', 66, '2016-4-4', 9012],
[6, 'Flynnv5', 19, '2016-5-5', 2131]]

conn.executemany(myTuple, records_to_insert)

record = conn.execute("SELECT id, name, age, DOB, postcode FROM CUSTOMERS")

for row in record:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("AGE = ", row[2])
    print("DOB = ", row[3],)
    print("POSTCODE = ", row[4], '\n')

conn.close()