import DataConn
from datetime import datetime

DataConn.dbConn()
con = DataConn.con
cur = DataConn.cur
res = DataConn.res

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_string(prompt):
    return input(prompt).strip()

def show_items():
    print("Items in the shop:")
    cur.execute("SELECT * FROM cs")
    for serial_no, product, cost in cur.fetchall():
        print(f"{serial_no}:\t{product}\t\tcost: {cost}")

def update_item_cost():
    sno = get_string("Enter the S.No of product: ")
    try:
        n_cost = float(input("Enter the amount to be added to cost: "))
        cur.execute("UPDATE cs SET cost = cost + %s WHERE sno = %s", (n_cost, sno))
        con.commit()
        print("Updated item cost successfully.")
        show_items()
    except Exception as e:
        print("Error:", e)

def add_variety():
    sno = get_string("Enter S.No: ")
    variety = get_string("Enter variety: ")
    try:
        cur.execute("INSERT INTO vip (sno, varieties) VALUES (%s, %s)", (sno, variety))
        con.commit()
        print("Variety added successfully.")
    except Exception as e:
        print("Error:", e)

def add_worker():
    cur.execute("SELECT MAX(Sno) FROM worker")
    r = cur.fetchone()
    sno = (r[0] + 1) if r[0] else 1
    name = get_string("Enter name: ")
    salary = get_int("Enter salary: ")
    try:
        cur.execute("INSERT INTO worker (Sno, Name, Salary) VALUES (%s, %s, %s)", (sno, name, salary))
        con.commit()
        print("Worker added successfully.")
    except Exception as e:
        print("Error:", e)

def show_workers():
    print("Workers in the shop:")
    cur.execute("SELECT * FROM worker")
    for sno, name, salary in cur.fetchall():
        print(f"{sno}:\t{name}\t\tsalary: {salary}")

def update_salary():
    name = get_string("Enter the employee name: ")
    choice = get_int("1. Increase Salary\n2. Decrease Salary\nEnter choice (1/2): ")
    amount = get_int("Enter amount: ")
    try:
        if choice == 1:
            cur.execute("UPDATE worker SET salary = salary + %s WHERE name = %s", (amount, name))
        elif choice == 2:
            cur.execute("UPDATE worker SET salary = salary - %s WHERE name = %s", (amount, name))
        else:
            print("Invalid choice.")
            return
        con.commit()
        print("Salary updated successfully.")
        show_workers()
    except Exception as e:
        print("Error:", e)

def add_item():
    sno = get_int("Enter S.No: ")
    product = get_string("Enter product name: ")
    cost = get_int("Enter cost: ")
    try:
        cur.execute("INSERT INTO cs (sno, products, cost) VALUES (%s, %s, %s)", (sno, product, cost))
        con.commit()
        print("Item added successfully.")
    except Exception as e:
        print("Error:", e)

def AdminFunc():
    admin = get_string("Enter username: ")
    password = get_int("Enter password: ")
    if password == 1234:
        while True:
            print("""
********* Hello Sir, You Logged In As Admin Successfully *********
1. Add item to shop
2. See items in shop
3. Update item cost
4. Add cake varieties
5. Add worker
6. View workers
7. Update worker salary
8. Sign out
""")
            choice = get_int("Enter your choice: ")
            if choice == 1:
                add_item()
            elif choice == 2:
                show_items()
            elif choice == 3:
                update_item_cost()
            elif choice == 4:
                add_variety()
            elif choice == 5:
                add_worker()
            elif choice == 6:
                show_workers()
            elif choice == 7:
                update_salary()
            elif choice == 8:
                print("Signing out...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")
    else:
        print("Wrong Password. Access Denied.")
