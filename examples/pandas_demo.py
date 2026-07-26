import pandas as pd

data = {
    "Expense ID": [1, 2, 3],
    "Category": ["Food", "Travel", "Movie"],
    "Amount": [200, 400, 300]
}

df = pd.DataFrame(data)

print(df)