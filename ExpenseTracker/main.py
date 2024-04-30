from handler import ExpenseTracker
import time

print("Welcome to Expense Tracker: ")
tracker = ExpenseTracker('expenses.json')

while True:
    time.sleep(2)
    print("Categories\n1. Insert Expense\n2. Delete Expense\n3. View All Expenses\n4. Get Expenses By Date\n5. Get "
          "Expense By Category\n6. Get the Total Expenses\n7. Get All the Categories of Expenses\n8. Exit")
    try:
        choice = int(input("Enter the Category number: "))
    except ValueError:
        print("Please enter a valid integer.")
    else:
        if choice == 1:
            category = input("What is the Category of the Expense: ").title()
            money = int(input("Enter the Money Spent: "))
            date = input("Enter the date in 'YYYY-MM-DD' Format: ")
            try:
                tracker.add_expense(category=category, amount=money, date=date)
                print("Expense added successfully.")
            except ValueError:
                print("Invalid input for amount. Please enter a valid number.")
            except Exception as e:
                print(f"An error occurred: {e}")

        elif choice == 2:
            category = input("What is the Category of the Expense you want to Delete: ").title()
            tracker.remove_expense_by_category(category=category)
            print("{} Category Removed".format(category))

        elif choice == 3:
            print("All Expenses")
            tracker.print_all_expenses()

        elif choice == 4:
            date = input("Enter the date in 'YYYY-MM-DD' Format: ")
            tracker.get_expenses_by_date(date=date)

        elif choice == 5:
            category = input("What is the Category of the Expense: ").title()
            tracker.print_expenses_by_category(category=category)

        elif choice == 6:
            total = tracker.get_total_expenses()
            print("Total Expenses are ", total)

        elif choice == 7:
            category = tracker.get_categories()
            for c in category:
                print(c, end=" ")
                print()

        elif choice == 8:
            print("See you Later.....")
            break

        else:
            print("Invalid Input..Please Enter valid input.")
