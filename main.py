
import json
import os
from pathlib import Path
from datetime import datetime
from collections import defaultdict


class Expense:

    def __init__(self, expense_id, title, amount, category, date, description=""):
        self.expense_id = expense_id
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def to_dict(self):
        return {
            "expense_id": self.expense_id,
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
    

class Storage:

    EXPENSE_FILE = "expenses.json"
    BUDGET_FILE = "budget.json"

    @staticmethod
    def load_expenses():
        expense_path = Path(Storage.EXPENSE_FILE)
        try:
            if not expense_path.exists():
                return []

            with open(Storage.EXPENSE_FILE, "r") as file:
                data = json.load(file)

            return [Expense.from_dict(item) for item in data]

        except (json.JSONDecodeError, TypeError, KeyError):
            print("Error reading expense file.")
            return []

    @staticmethod
    def save_expenses(expenses):
        with open(Storage.EXPENSE_FILE, "w") as file:
            json.dump(
                [expense.to_dict() for expense in expenses],
                file,
                indent=4
            )

    @staticmethod
    def load_budget():
        try:
            if not os.path.exists(Storage.BUDGET_FILE):
                return 0

            with open(Storage.BUDGET_FILE, "r") as file:
                return float(json.load(file).get("monthly_budget", 0))

        except (json.JSONDecodeError, TypeError, ValueError):
            return 0

    @staticmethod
    def save_budget(amount):
        with open(Storage.BUDGET_FILE, "w") as file:
            json.dump({"monthly_budget": amount}, file, indent=4)


class ExpenseManager:

    def __init__(self):
        self.expenses = Storage.load_expenses()
        self.budget = Storage.load_budget()

    def generate_id(self):
        if not self.expenses:
            return 1

        return max(e.expense_id for e in self.expenses) + 1

    def add_expense(self):

        print("\n--- ADD EXPENSE ---")

        title = input("Enter title: ").strip()

        if not title:
            print("Title cannot be empty.")
            return

        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                return

        except ValueError:
            print("Invalid amount.")
            return

        category = input("Enter category: ").strip()

        if not category:
            print("Category cannot be empty.")
            return

        date = input("Enter date (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format.")
            return

        description = input("Enter description: ").strip()

        expense = Expense(
            self.generate_id(),
            title,
            amount,
            category,
            date,
            description
        )

        self.expenses.append(expense)
        Storage.save_expenses(self.expenses)

        print("Expense added successfully!")

    def view_expenses(self):

        print("\n--- ALL EXPENSES ---")

        if not self.expenses:
            print("No expenses found.")
            return

        for expense in sorted(self.expenses, key=lambda e: e.date):

            print(f"""
ID: {expense.expense_id}
Title: {expense.title}
Amount: ₹{expense.amount:.2f}
Category: {expense.category}
Date: {expense.date}
Description: {expense.description}
--------------------------
""")

    def search_by_category(self):

        category = input("Enter category: ").strip().lower()

        results = [
            e for e in self.expenses
            if e.category.lower() == category
        ]

        if not results:
            print("No expenses found.")
            return

        for expense in results:
            print(expense.to_dict())

    def search_by_date(self):

        date = input("Enter date (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date.")
            return

        results = [e for e in self.expenses if e.date == date]

        if not results:
            print("No expenses found.")
            return

        for expense in results:
            print(expense.to_dict())

    def update_expense(self):

        try:
            expense_id = int(input("Enter expense ID to update: "))
        except ValueError:
            print("Invalid ID.")
            return

        expense = next(
            (e for e in self.expenses if e.expense_id == expense_id),
            None
        )

        if expense is None:
            print("Expense not found.")
            return

        print("Leave blank to keep the existing value.")

        title = input(f"New title [{expense.title}]: ").strip()
        amount = input(f"New amount [{expense.amount}]: ").strip()
        category = input(f"New category [{expense.category}]: ").strip()
        date = input(f"New date [{expense.date}]: ").strip()
        description = input(
            f"New description [{expense.description}]: "
        ).strip()

        if title:
            expense.title = title

        if amount:
            try:
                new_amount = float(amount)
                if new_amount <= 0:
                    print("Amount must be positive.")
                    return
                expense.amount = new_amount
            except ValueError:
                print("Invalid amount.")
                return

        if category:
            expense.category = category

        if date:
            try:
                datetime.strptime(date, "%Y-%m-%d")
                expense.date = date
            except ValueError:
                print("Invalid date.")
                return

        if description:
            expense.description = description

        Storage.save_expenses(self.expenses)

        print("Expense updated successfully!")

    def delete_expense(self):

        try:
            expense_id = int(input("Enter expense ID to delete: "))
        except ValueError:
            print("Invalid ID.")
            return

        expense = next(
            (e for e in self.expenses if e.expense_id == expense_id),
            None
        )

        if expense is None:
            print("Expense not found.")
            return

        self.expenses.remove(expense)
        Storage.save_expenses(self.expenses)

        print("Expense deleted successfully!")

    def total_expenses(self):

        total = sum(e.amount for e in self.expenses)

        print(f"\nTotal expenses: ₹{total:.2f}")

    def monthly_expenses(self):

        month = input("Enter month (YYYY-MM): ").strip()

        try:
            datetime.strptime(month, "%Y-%m")
        except ValueError:
            print("Invalid month.")
            return

        total = sum(
            e.amount for e in self.expenses
            if e.date.startswith(month)
        )

        print(f"Total expenses for {month}: ₹{total:.2f}")

    def category_summary(self):

        summary = defaultdict(float)

        for expense in self.expenses:
            summary[expense.category] += expense.amount

        print("\n--- CATEGORY SUMMARY ---")

        if not summary:
            print("No expenses available.")
            return

        for category, amount in summary.items():
            print(f"{category}: ₹{amount:.2f}")

    def set_budget(self):

        try:
            amount = float(input("Enter monthly budget: "))

            if amount <= 0:
                print("Budget must be positive.")
                return

            self.budget = amount
            Storage.save_budget(amount)

            print("Budget saved successfully!")

        except ValueError:
            print("Invalid budget.")

    def check_budget(self):

        month = datetime.today().strftime("%Y-%m")

        total = sum(
            e.amount for e in self.expenses
            if e.date.startswith(month)
        )

        print(f"\nMonthly budget: ₹{self.budget:.2f}")
        print(f"Amount spent: ₹{total:.2f}")
        print(f"Remaining: ₹{self.budget - total:.2f}")

        if self.budget == 0:
            print("Set a budget first.")

        elif total > self.budget:
            print("WARNING: Monthly budget exceeded!")

        else:
            print("You are within your budget.")


def main():

    manager = ExpenseManager()

    while True:

        print("""
================================
       EXPENSE TRACKER
================================

1. Add Expense
2. View All Expenses
3. Search by Category
4. Search by Date
5. Update Expense
6. Delete Expense
7. Total Expenses
8. Monthly Expenses
9. Category Summary
10. Set Monthly Budget
11. Check Monthly Budget
0. Exit

================================
""")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            manager.add_expense()

        elif choice == "2":
            manager.view_expenses()

        elif choice == "3":
            manager.search_by_category()

        elif choice == "4":
            manager.search_by_date()

        elif choice == "5":
            manager.update_expense()

        elif choice == "6":
            manager.delete_expense()

        elif choice == "7":
            manager.total_expenses()

        elif choice == "8":
            manager.monthly_expenses()

        elif choice == "9":
            manager.category_summary()

        elif choice == "10":
            manager.set_budget()

        elif choice == "11":
            manager.check_budget()

        elif choice == "0":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
