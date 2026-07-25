from models.expense import Expense


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

    def sort_expenses(self) -> None:
        sorted_expenses = sorted(
            self.expenses,
            key=lambda expense: expense.amount
        )

        print("\nExpenses Sorted by Amount")
        print("=" * 35)

        for expense in sorted_expenses:
            expense.display()