from dataclasses import dataclass

@dataclass
class Expense:

    expense_id: int
    category: str
    amount: float
    transaction_type: str
    transaction_date: str

    def display(self) -> None:

        print("-" * 35)
        print("Expense ID :", self.expense_id)
        print("Category   :", self.category)
        print("Amount     :", self.amount)
        print("Type       :", self.transaction_type)
        print("Date       :", self.transaction_date)