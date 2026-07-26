
import csv
import json
import configparser
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
        """Save expenses to CSV."""

        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Expense ID",
                "Category",
                "Amount",
                "Type"
            ])

            for expense in self.expenses:
                writer.writerow([
                    expense.expense_id,
                    expense.category,
                    expense.amount,
                    expense.transaction_type
                ])

        print("Expenses saved to CSV successfully!")

    def load_from_csv(self) -> None:
        """Load expenses from CSV."""

        self.expenses.clear()

        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)

            next(reader)  # Skip header

            for row in reader:
                expense = Expense(
                    int(row[0]),
                    row[1],
                    float(row[2]),
                    row[3]
                )
                self.expenses.append(expense)

        print("Expenses loaded from CSV successfully!")

    def save_to_json(self) -> None:
        """Save expenses to JSON."""

        data = []

        for expense in self.expenses:
            data.append({
                "expense_id": expense.expense_id,
                "category": expense.category,
                "amount": expense.amount,
                "transaction_type": expense.transaction_type
            })

        with open(JSON_FILE, "w") as file:
            json.dump(data, file, indent=4)

        print("Expenses saved to JSON successfully!")

    def load_from_json(self) -> None:
        """Load expenses from JSON."""

        self.expenses.clear()

        with open(JSON_FILE, "r") as file:
            data = json.load(file)

        for item in data:
            expense = Expense(
                item["expense_id"],
                item["category"],
                item["amount"],
                item["transaction_type"]
            )
            self.expenses.append(expense)

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

    def expense_statistics(self) -> None:

        if not self.expenses:
            print("No expenses available.")
            return

        amounts = []

        for expense in self.expenses:
            amounts.append(expense.amount)

        expense_array = np.array(amounts)

        print("\nExpense Statistics")
        print("=" * 35)
        print(f"Total Expense   : {np.sum(expense_array):.2f}")
        print(f"Average Expense : {np.mean(expense_array):.2f}")
        print(f"Maximum Expense : {np.max(expense_array):.2f}")
        print(f"Minimum Expense : {np.min(expense_array):.2f}")

    def view_dataframe(self) -> None:
        """Display expenses using pandas DataFrame."""

        if not self.expenses:
            print("No expenses available.")
            return

        data = {
            "Expense ID": [],
            "Category": [],
            "Amount": [],
            "Type": []
        }

        for expense in self.expenses:
            data["Expense ID"].append(expense.expense_id)
            data["Category"].append(expense.category)
            data["Amount"].append(expense.amount)
            data["Type"].append(expense.transaction_type)

        df = pd.DataFrame(data)

        print("\nExpenses DataFrame")
        print("=" * 40)
        print(df)

    def income_expense_summary(self) -> None:
        """Display Income vs Expense Summary."""

        if not self.expenses:
            print("No transactions available.")
            return

        data = {
            "Category": [],
            "Amount": [],
            "Type": []
        }

        for expense in self.expenses:
            data["Category"].append(expense.category)
            data["Amount"].append(expense.amount)
            data["Type"].append(expense.transaction_type)

        df = pd.DataFrame(data)

        income = df[df["Type"].str.lower() == "income"]["Amount"].sum()
        expense = df[df["Type"].str.lower() == "expense"]["Amount"].sum()

        print("\nIncome vs Expense Summary")
        print("=" * 40)
        print(f"Total Income  : ₹{income:.2f}")
        print(f"Total Expense : ₹{expense:.2f}")
        print("-" * 40)
        print(f"Balance       : ₹{income - expense:.2f}")

    def filter_by_type(self) -> None:
        """Filter transactions by type."""

        if not self.expenses:
            print("No transactions available.")
            return

        transaction_type = input("Enter Type (Income/Expense): ")

        data = {
            "Expense ID": [],
            "Category": [],
            "Amount": [],
            "Type": []
        }

        for expense in self.expenses:
            data["Expense ID"].append(expense.expense_id)
            data["Category"].append(expense.category)
            data["Amount"].append(expense.amount)
            data["Type"].append(expense.transaction_type)

        df = pd.DataFrame(data)

        filtered = df[
            df["Type"].str.lower() == transaction_type.lower()
            ]

        print("\nFiltered Transactions")
        print("=" * 40)

        if filtered.empty:
            print("No records found.")
        else:
            print(filtered)

    def category_summary(self):

        data = []

        for expense in self.expenses:
            data.append({
                "Expense ID": expense.expense_id,
                "Category": expense.category,
                "Amount": expense.amount,
                "Type": expense.transaction_type
            })

        # Step 3: Create DataFrame
        df = pd.DataFrame(data)

        # Step 4: GroupBy
        summary = df.groupby("Category")["Amount"].sum()

        # Step 5: Display Result
        print("\nCategory-wise Summary")
        print("========================")
        print(summary)

    def expense_bar_chart(self):

        data = []

        for expense in self.expenses:
            data.append({
                "Category": expense.category,
                "Amount": expense.amount
            })

        df = pd.DataFrame(data)

        summary = df.groupby("Category")["Amount"].sum()

        summary.plot(kind="bar")

        plt.title("Expense by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Amount")

        plt.show()

    def expense_pie_chart(self):

        data = []

        for expense in self.expenses:
            data.append({
                "Category": expense.category,
                "Amount": expense.amount
            })

        df = pd.DataFrame(data)

        summary = df.groupby("Category")["Amount"].sum()

        plt.figure(figsize=(6, 6))

        plt.pie(
            summary,
            labels=summary.index,
            autopct="%1.1f%%",
            startangle=90
        )

        plt.title("Expense Distribution by Category")

        plt.show()

    def analytics_dashboard(self):

        print("\n========================================")
        print("      ANALYTICS DASHBOARD")
        print("========================================")

        print("\n1. Expense Statistics")
        self.expense_statistics()

        print("\n2. Category-wise Summary")
        self.category_summary()

        print("\n3. Income vs Expense Summary")
        self.income_expense_summary()

        print("\n4. Expense DataFrame")
        self.view_dataframe()

        print("\n5. Expense Bar Chart")
        self.expense_bar_chart()

        print("\n6. Expense Pie Chart")
        self.expense_pie_chart()