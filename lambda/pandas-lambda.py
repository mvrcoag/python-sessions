import pandas as pd

df = pd.DataFrame({"name": ["Marco", "Juan", "Pedro", "Ana"], "age": [21, 34, 18, 23]})

# 60


def formal_name(x):
    if x == "Ana":
        return f"Ms. {x}"
    return f"Mr. {x}"


df["left_years"] = df["age"].apply(lambda x: 60 - x)
df["formal_name"] = df["name"].apply(formal_name)

print(df)
