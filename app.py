from models.expense import Expense
from services.expense_service import ExpenseService


def display_menu() -> None:
    print("\n" + "=" * 40)
    print("      DATASENSE FINANCE")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")


def main() -> None:

    service = ExpenseService()

    while True:

        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":

            expense_id = int(input("Enter Expense ID: "))
            category = input("Enter Category: ")
            amount = float(input("Enter Amount: "))

            expense = Expense(
                expense_id,
                category,
                amount
            )

            service.add_expense(expense)

        elif choice == "2":

            service.view_expenses()

        elif choice == "3":

            print("Thank You!")
            break

        else:

            print("Invalid Choice")


if __name__ == "__main__":
    main()