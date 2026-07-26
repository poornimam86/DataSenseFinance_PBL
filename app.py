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
    print("7. Save Expenses to JSON")
    print("8. Load Expenses from JSON")
    print("9.Category Count Report")
    print("10. Category Count Report")
    print("11. Exit")


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
            service.save_to_json()

        elif choice == "8":
            service.load_from_json()

        elif choice == "9":
            service.category_count()
        elif choice == "10":
            service.category_amount_report()
        elif choice == "11":

            print("Thank You!")

            break
        else:

            print("Invalid Choice")


if __name__ == "__main__":
    main()