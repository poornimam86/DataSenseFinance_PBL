
import csv
import json
import configparser

from pathlib import Path
from models.expense import Expense
from collections import Counter, defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent
# Create ConfigParser object
config = configparser.ConfigParser()
config.read(BASE_DIR / "config" / "config.ini")


TEXT_FILE = Path(config["Files"]["text"])
CSV_FILE = Path(config["Files"]["csv"])
JSON_FILE = Path(config["Files"]["json"])
class ExpenseService:
    """Handles expense operations."""

    def __init__(self) -> None:
        self.expenses = []

    def add_expense(self, expense: Expense) -> None:
        self.expenses.append(expense)
        print("Expense Added Successfully!")

    def view_expenses(self) -> None:
        """Display all expenses."""

        if not self.expenses:
            print("No Expenses Found.")
            return

        print("\nExpense List")
        print("=" * 35)

        for expense in self.expenses:
            expense.display()

    def save_to_file(self) -> None:
        """Save expenses to a text file."""

        with open(TEXT_FILE, "w") as file:

            for expense in self.expenses:
                file.write(f"Expense ID : {expense.expense_id}\n")
                file.write(f"Category   : {expense.category}\n")
                file.write(f"Amount     : {expense.amount}\n")
                file.write("-" * 30 + "\n")

        print("Expenses Saved Successfully!")

    def save_to_csv(self) -> None:

        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)

            # Header
            writer.writerow(["Expense ID", "Category", "Amount"])

            # Data
            for expense in self.expenses:
                writer.writerow([
                    expense.expense_id,
                    expense.category,
                    expense.amount
                ])

        print("Expenses saved to CSV successfully!")

    def load_from_csv(self) -> None:

        import csv

        self.expenses.clear()

        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)

            next(reader)  # Skip header

            for row in reader:
                expense = Expense(
                    row[0],  # Expense ID
                    row[1],  # Category
                    float(row[2])  # Amount
                )

                self.expenses.append(expense)

        print("Expenses loaded from CSV successfully!")

    def save_to_json(self) -> None:

        expense_list = []

        for expense in self.expenses:
            expense_list.append({
                "expense_id": expense.expense_id,
                "category": expense.category,
                "amount": expense.amount
            })

        with open(JSON_FILE, "w") as file:
            json.dump(expense_list, file, indent=4)

        print("Expenses saved to JSON successfully!")

    def load_from_json(self) -> None:

        self.expenses.clear()

        with open(JSON_FILE, "r") as file:
            expense_list = json.load(file)

        for expense in expense_list:
            new_expense = Expense(
                expense["expense_id"],
                expense["category"],
                expense["amount"]
            )

            self.expenses.append(new_expense)

        print(f"{len(self.expenses)} expenses loaded from JSON successfully!")

    def sort_expenses(self) -> None:
        sorted_expenses = sorted(
            self.expenses,
            key=lambda expense: expense.amount
        )

        print("\nExpenses Sorted by Amount")
        print("=" * 35)

        for expense in sorted_expenses:
            expense.display()

    def category_count(self) -> None:

        categories = []

        for expense in self.expenses:
            categories.append(expense.category)

        counter = Counter(categories)

        print("\nCategory Report")
        print("=" * 30)

        for category, count in counter.items():
            print(f"{category} : {count}")

    def category_amount_report(self) -> None:

        category_total = defaultdict(float)

        for expense in self.expenses:
            category_total[expense.category] += expense.amount

        print("\nCategory-wise Amount Report")
        print("=" * 35)

        for category, amount in category_total.items():
            print(f"{category} : ₹{amount:.2f}")