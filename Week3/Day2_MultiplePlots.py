##Create two or three separate charts and note the purpose of each chart.##
import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 120, 150, 130, 180]

subjects = ["Math", "Science", "English", "History"]
marks = [85, 90, 78, 88]

data = np.random.randint(40, 101, 50)

plt.figure()
plt.plot(months, sales)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

plt.figure()
plt.bar(subjects, marks)
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(axis="y")
plt.show()

plt.figure()
plt.hist(data, bins=5)
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.grid(axis="y")
plt.show()