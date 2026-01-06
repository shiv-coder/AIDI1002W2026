# STEP 1: Import required libraries
import matplotlib.pyplot as plt
import numpy as np
 
 
# STEP 2: Create a basic dataset
students = ["Alex", "John", "Sara", "Emma"]
marks = [85, 90, 78, 88]
 
 
# STEP 3: Line Plot
plt.figure()
plt.plot(students, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks - Line Plot")
plt.show()
 
 
# STEP 4: Bar Chart
plt.figure()
plt.bar(students, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks - Bar Chart")
plt.show()
 
 
# STEP 5: Scatter Plot
plt.figure()
plt.scatter(students, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks - Scatter Plot")
plt.show()
 
 
# STEP 6: Histogram
plt.figure()
plt.hist(marks, bins=5)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Marks Distribution - Histogram")
plt.show()