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
    print("10. Category_wise Summary")
    print("11. Expense Statistics(NumPy)")
    print("12. View Expenses as DataFrame")
    print("13. Income vs Expense Summary")
    print("14. Filter by Trasaction Type")
    print("15. Expense Bar Chart")
    print("16. Expense Pie Chart ")
    print("17. Analystics Dashboard ")
    print("18. Visual Dashboard ")
    print("19. Exit")



def main() -> None:

    service = ExpenseService()

    while True:

        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":

            expense_id = int(input("Enter Expense ID: "))
            category = input("Enter Category: ")
            amount = float(input("Enter Amount: "))
            transaction_type = input("Enter Type (Income/Expense): ")
            transaction_date = input("Enter Transaction Date (DD-MM-YYYY): ")

            expense = Expense(
                expense_id,
                category,
                amount,
                transaction_type,
                transaction_date
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
            service.category_summary()

        elif choice == "11":
            service.expense_statistics()


        elif choice == "12":
            service.view_dataframe()

        elif choice == "13":
            service.income_expense_summary()

        elif choice == "14":
            service.filter_by_type()

        elif choice == "15":
            service.expense_bar_chart()

        elif choice == "16":
            service.expense_pie_chart()

        elif choice == "17":
            service.analytics_dashboard()

        elif choice == "18":
            service.visual_dashboard()

        elif choice == "19":
            print("Thank YOu!")

            break
        else:

            print("Invalid Choice")


if __name__ == "__main__":
    main()