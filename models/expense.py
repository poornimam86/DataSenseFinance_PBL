class Expense:
    """Represents one expense."""

    def __init__(
        self,
        expense_id: int,
        category: str,
        amount: float
    ) -> None:

        self.expense_id = expense_id
        self.category = category
        self.amount = amount

    def display(self) -> None:
        """Display expense details."""

        print("-" * 35)
        print("Expense ID :", self.expense_id)
        print("Category   :", self.category)
        print("Amount     :", self.amount)