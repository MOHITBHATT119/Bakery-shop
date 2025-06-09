import mysql.connector

con = mysql.connector.connect(host='localhost', user='root', password='root')
cur = con.cursor()
res = ""

def dbConn():
    cur.execute("CREATE DATABASE IF NOT EXISTS items")
    cur.execute("USE items")

    # Create and seed product table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS cs (
            sno INT PRIMARY KEY,
            products VARCHAR(20),
            cost INT
        )
    """)
    cur.execute("SELECT * FROM cs")
    if not cur.fetchall():
        cur.executemany("INSERT INTO cs VALUES (%s, %s, %s)", [
            (1, 'Cake', 50),
            (2, 'Pastry', 20),
            (3, 'Milk', 60),
            (4, 'Butter', 20),
            (5, 'Cheese', 30)
        ])
        con.commit()

    # Create and seed variety table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS vip (
            sno INT,
            varieties VARCHAR(30)
        )
    """)
    cur.execute("SELECT * FROM vip")
    if not cur.fetchall():
        cur.executemany("INSERT INTO vip VALUES (%s, %s)", [
            (1, 'Vanilla'),
            (2, 'Chocolate'),
            (3, 'Strawberry'),
            (4, 'Butterscotch')
        ])
        con.commit()

    # Create and seed workers table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS worker (
            Sno INT PRIMARY KEY,
            Name VARCHAR(20),
            Salary INT
        )
    """)
    cur.execute("SELECT * FROM worker")
    if not cur.fetchall():
        cur.executemany("INSERT INTO worker VALUES (%s, %s, %s)", [
            (1, 'Mukesh', 12364),
            (2, 'Ram', 1234),
            (3, 'Suresh', 23459),
            (4, 'Raju', 8987)
        ])
        con.commit()
