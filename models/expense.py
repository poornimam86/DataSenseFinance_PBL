from dataclasses import dataclass

@dataclass
class Expense:
    """Represents one expense."""

    expense_id: int
    category: str
    amount: float

    def display(self) -> None:
        """Display expense details."""

        print("-" * 35)
        print("Expense ID :", self.expense_id)
        print("Category   :", self.category)
        print("Amount     :", self.amount)