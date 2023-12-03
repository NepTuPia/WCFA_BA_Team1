import pandas as pd
import os

directory = "processed_raw_data/"

combined_data = pd.DataFrame()

for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)

        df = pd.read_csv(file_path, header=0)

        df = df.iloc[:, :-1]

        combined_data = pd.concat([combined_data, df], ignore_index=True)

print(combined_data)

combined_data.to_csv('combined_data.csv', index=False)
