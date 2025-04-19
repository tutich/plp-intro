import pandas as pd
# Example 2: Creating a DataFrame from a dictionary

data = { 
    "name": ["John Doe", "Jane Smith", "Emily Davis"],
    "age": [25, 30, 22],  
    "grades": [85, 90, 48],
}

df = pd.DataFrame(data)
df["passed"] = df["grades"] >= 50  # Adding a new column based on a condition

passed_students = df[df["passed"] == True]  # Filtering rows based on a condition
print("Passed Students:")
print(df)