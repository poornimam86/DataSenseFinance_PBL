def add_expense(category, amount, description="No Description"):
    print("Category    :", category)
    print("Amount      :", amount)
    print("Description :", description)


# Calling with all arguments
add_expense("Food", 300, "Lunch")

print()

# Calling without description
add_expense("Travel", 500)