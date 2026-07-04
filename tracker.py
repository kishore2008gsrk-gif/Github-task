expenses = []

while True:
    print("\nPersonal Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Expense name: ")
        amount = float(input("Amount: "))
        expenses.append([name, amount])
        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            print("\nExpenses:")
            for i, e in enumerate(expenses, 1):
                print(f"{i}. {e[0]} - ₹{e[1]}")

    elif choice == "3":
        total = sum(e[1] for e in expenses)
        print("Total Expense = ₹", total)

    elif choice == "4":
        if len(expenses) == 0:
            print("No expenses to delete.")
        else:
            for i, e in enumerate(expenses, 1):
                print(f"{i}. {e[0]} - ₹{e[1]}")
            num = int(input("Enter expense number to delete: "))
            if 1 <= num <= len(expenses):
                deleted = expenses.pop(num - 1)
                print(deleted[0], "deleted successfully!")
            else:
                print("Invalid number!")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")