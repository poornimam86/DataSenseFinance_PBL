def display_expense(**details):
    for key, value in details.items():
        print(key, ":", value)


display_expense(
    id=101,
    category="Food",
    amount=300
)