# STEP 1: Import pandas
import pandas as pd
 
# STEP 2: Create a DataFrame
data = {
    "Name": ["Alex", "John", "Mary"],
    "Age": [20, 21, 22],
    "Grade": [88, 92, 95]
}
 
 
 
# STEP 3: Display DataFrame
df = pd.DataFrame(data)
print(df)
 
# STEP 4: Read a CSV file 
# df2 = pd.read_csv("sample.csv")

#print(df.info)
#print(df.describe())
print(df["Name"])
print(df.loc[0])