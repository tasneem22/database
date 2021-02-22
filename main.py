import psycopg2
from faker import Faker




if __name__ == '__main__':
    print("Database is going to be opened")

    con = psycopg2.connect(database="customers", user="postgres", password="postgres", host="127.0.0.1", port="5433")
    print("Database opened successfully")
    cur = con.cursor()
    cur.execute('''CREATE TABLE CUSTOMER
       (ID INT PRIMARY KEY    NOT NULL,
       Name           TEXT    NOT NULL,
       Address        TEXT    NOT NULL,
       Age             INT  NOT NULL,
       review        TEXT);''')
    print("Table created successfully")
    fake = Faker()
    for i in range(100000):
        cur.execute("INSERT INTO CUSTOMER (ID,Name,Address,Age,review) VALUES ('" + str(
            i) + "','" + fake.name() + "','" + fake.address() + "','" + str(fake.random_int(18, 100)) + "','" + fake.text() + "')")
        con.commit()

    cur = con.cursor()
    cur.execute('''CREATE TABLE CUSTOMERS
       (ID INT PRIMARY KEY    NOT NULL,
       Name           TEXT    NOT NULL,
       Address        TEXT    NOT NULL,
       Age             INT  NOT NULL,
       review        TEXT);''')
    print("Table created successfully")
    fake = Faker()
    for i in range(100000):
        cur.execute("INSERT INTO CUSTOMERS (ID,Name,Address,Age,review) VALUES ('" + str(
            i) + "','" + fake.name() + "','" + fake.address() + "','" + str(fake.random_int(18, 100)) + "','" + fake.text() + "')")
        con.commit()
