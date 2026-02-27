import pandas as pd
import os, sys

### Get Input File from Terminal

if len(sys.argv) < 2:
    print("Usage: python process_data.py <input_file>")
    exit()

file_name = sys.argv[1]
output_file = "cleaned_data.csv"

file_extension = os.path.splitext(file_name)[1]

if file_extension == ".csv":
    df = pd.read_csv(file_name)
elif file_extension == ".xlsx":
    df = pd.read_excel(file_name)
else:
    print("Unsupported file type!")
    exit()

print("Original Data")
print(df)



### Data Processing

# Remove duplicates
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

# Sort data by name
df = df.sort_values(by="name")


print("\nCleaned Data")
print(df)


### Save Output

df.to_csv(output_file, index=False)
print("\nCleaned data saved to:", output_file)