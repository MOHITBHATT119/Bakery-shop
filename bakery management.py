import DataConn
import AdminFile
import CustomerFile
from datetime import datetime

DataConn.dbConn()
con = DataConn.con
cur = DataConn.cur
res = DataConn.res

def main():
    print("--------------## CLASS 12TH IP PROJECT ##---------------")
    print("________________________________________________________")
    print("|................. WELCOME TO .........................|")
    print("|_______________ BAKERY MANAGEMENT SYSTEM ______________|")
    print("------------------ MADE BY : MOHIT BHATT ----------------")
    print(".................. SESSION : 2025-2026 ..................")

    while True:
        print("\nPlease choose:")
        print("1. Admin")
        print("2. Customer")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")
            continue

        if choice == 1:
            AdminFile.AdminFunc()
        elif choice == 2:
            CustomerFile.CustomerFunc()
        elif choice == 3:
            print("Thank you for using the Bakery Management System!")
            break
        else:
            print("Invalid choice. Please choose between 1 to 3.")

if __name__ == '__main__':
    main()
