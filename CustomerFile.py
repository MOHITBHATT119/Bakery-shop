from datetime import datetime
import DataConn

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

name = get_string("Enter your name: ")
phone = get_int("Enter your phone number: ")

def items():
    print("Items in the shop:")
    cur.execute('SELECT * FROM cs')
    for serial_no, product, cost in cur.fetchall():
        print(f"{serial_no}:\t{product}\t\tcost: {cost}")

def show_varieties():
    cur.execute('SELECT * FROM vip')
    varieties = cur.fetchall()
    print("Available Cake Varieties:")
    for sno, variety in varieties:
        print(f"{sno}. {variety}")
    return varieties

def order_cake():
    varieties = show_varieties()
    choice = get_int("Enter your choice of variety: ")
    qty = get_int("Enter quantity: ")

    if 1 <= choice <= len(varieties):
        variety = varieties[choice - 1][1]
        cur.execute("SELECT cost FROM cs WHERE products='Cake'")
        result = cur.fetchone()
        if result:
            cost = qty * result[0]
            print(f"\nYou have successfully ordered {qty} {variety} cake(s). Total cost: {cost}")
            print_bill(name, phone, variety, qty, cost)
    else:
        print("Invalid cake choice.")

def print_bill(name, phone, item, qty, total):
    print("\n--------------------- BILL ---------------------")
    print(f"Customer Name: {name}")
    print(f"Phone: {phone}")
    print(f"Item: {item}")
    print(f"Quantity: {qty}")
    print(f"Total Amount: Rs. {total}")
    print("@@@@ THANK YOU FOR ORDERING @@@@")
    print(f"Date: {datetime.now()}\n")

def order():
    items()
    sno = get_int("Enter the S.No of the item to order: ")

    cur.execute("SELECT products, cost FROM cs WHERE sno = %s", (sno,))
    row = cur.fetchone()
    if not row:
        print("Invalid item number.")
        return

    product, unit_price = row
    if product.lower() == 'cake':
        order_cake()
    else:
        qty = get_int(f"Enter quantity of {product}: ")
        total = qty * unit_price
        print(f"\nYou have successfully ordered {qty} {product}(s). Total cost: {total}")
        print_bill(name, phone, product, qty, total)

def CustomerFunc():
    print('1. View Menu')
    print('2. Order Item')
    choice = get_int("Enter your choice: ")

    if choice == 1:
        items()
    elif choice == 2:
        order()
    else:
        print("Invalid choice.")
