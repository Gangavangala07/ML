import pandas as pd

data = {
    'Age': [25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46],
    'Rating': [4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65]
}

df = pd.DataFrame(data)

mean_values = df.mean()
print("Mean Values in the Distribution:")
print(mean_values)

median_values = df.median()
print("\nMedian Values in the Distribution:")
print(median_values)

mode_values = df.mode()
print("\nMode Values in the Distribution:")
print(mode_values)

variance = df.var()
std_deviation = df.std()
print("\nVariance:")
print(variance)
print("\nStandard Deviation:")
print(std_deviation)
