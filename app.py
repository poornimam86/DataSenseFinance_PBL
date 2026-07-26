from models.expense import Expense
from services.expense_service import ExpenseService


def display_menu() -> None:
    print("\n" + "=" * 40)
    print("      DATASENSE FINANCE")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Sort Expenses by Amount")
    print("4. Save Expenses to File")
    print("5. Save Expenses to CSV")
    print("6. Load Expenses from CSV")
    print("7. Exit")


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
            service.sort_expenses()

        elif choice == "4":
            service.save_to_file()


        elif choice == "5":

            service.save_to_csv()

        elif choice == "6":
            service.load_from_csv()

        elif choice == "7":

            print("Thank You!")

            break
        else:

            print("Invalid Choice")


if __name__ == "__main__":
    main()