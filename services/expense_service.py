from models.expense import Expense
import csv

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

        with open("data/expenses.txt", "w", encoding="utf-8") as file:

            for expense in self.expenses:
                file.write(f"Expense ID : {expense.expense_id}\n")
                file.write(f"Category   : {expense.category}\n")
                file.write(f"Amount     : {expense.amount}\n")
                file.write("-" * 30 + "\n")

        print("Expenses Saved Successfully!")

    def save_to_csv(self) -> None:

        with open("data/expenses.csv", "w", newline="") as file:
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

        with open("data/expenses.csv", "r") as file:
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

    def sort_expenses(self) -> None:
        sorted_expenses = sorted(
            self.expenses,
            key=lambda expense: expense.amount
        )

        print("\nExpenses Sorted by Amount")
        print("=" * 35)

        for expense in sorted_expenses:
            expense.display()