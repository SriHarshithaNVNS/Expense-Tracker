import json
from datetime import datetime


class ExpenseTracker:
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(self.filename, "r") as json_file:
                self.data = json.load(json_file)

        except FileNotFoundError:
            self.data = {"expenses": []}

    def add_expense(self, category, amount, date=None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        self.data["expenses"].append({"category": category, "amount": amount, "date": date})
        self._save_data()

    def remove_expense_by_category(self, category):
        categories = self.get_categories()
        if category in categories:
            self.data["expenses"] = [expense for expense in self.data["expenses"] if expense["category"] != category]
            self._save_data()
        else:
            print("{} Category does not Exist".format(category))

    def print_all_expenses(self):
        for expense in self.data["expenses"]:
            print(f"Category: {expense['category']}, Amount: {expense['amount']}, Date: {expense['date']}")

    def get_expenses_by_date(self, date):
        expenses_on_date = [expense for expense in self.data["expenses"] if expense["date"] == date]
        print(f"Expenses on {date}:")
        for expense in expenses_on_date:
            print(f"Category: {expense['category']}, Amount: {expense['amount']}, Date: {expense['date']}")

    def print_expenses_by_category(self, category):
        category_expenses = [expense for expense in self.data["expenses"] if expense["category"] == category]
        if not category_expenses:
            print("No expenses found for this category.")
        else:
            print(f"Expenses for Category '{category}':")
            for expense in category_expenses:
                print(f"Amount: {expense['amount']}, Date: {expense['date']}")

    def _save_data(self):
        with open(self.filename, "w") as json_file:
            json.dump(self.data, json_file, indent=4)

    def get_total_expenses(self):
        total = sum(expense["amount"] for expense in self.data["expenses"])
        return total

    def get_categories(self):
        return set(expense["category"] for expense in self.data["expenses"])


