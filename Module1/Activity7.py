# STEP 1: Import required libraries
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
 
 
# STEP 2: Create a basic dataset
data = {
    "Student": ["Alex", "John", "Sara", "Emma"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 90, 78, 88]
}
 
df = pd.DataFrame(data)
 
 
# STEP 3: Bar Plot
plt.figure()
sns.barplot(x="Student", y="Marks", data=df)
plt.title("Student Marks - Bar Plot (Seaborn)")
plt.show()
 
 
# STEP 4: Scatter Plot
plt.figure()
sns.scatterplot(x="Age", y="Marks", data=df)
plt.title("Age vs Marks - Scatter Plot")
plt.show()
 
 
# STEP 5: Histogram
plt.figure()
sns.histplot(df["Marks"], bins=5)
plt.title("Marks Distribution - Histogram")
plt.show()
 
 
# STEP 6: Box Plot
plt.figure()
sns.boxplot(y="Marks", data=df)
plt.title("Marks Spread - Box Plot")
plt.show()