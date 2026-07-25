class Expense:
    def display(self):
        print("Displaying Expense Details")


class Income:
    def display(self):
        print("Displaying Income Details")


def show_details(item):
    item.display()


expense = Expense()
income = Income()

show_details(expense)
show_details(income)