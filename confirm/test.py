import pandas as pd

# Example DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [6, 7, 8, 9, 10]
}
df = pd.DataFrame(data)

# Calculate mean of each column
mean_values = df.mean()

# Calculate squared deviation for each column
squared_deviations = (df - mean_values) ** 2

print("Squared deviations from mean:")
print(squared_deviations)
