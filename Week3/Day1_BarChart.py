##Build a bar chart using categories and values.##
import matplotlib.pyplot as plt

categories = ["Math", "Science", "English", "History", "Computer"]
values = [85, 90, 78, 88, 95]

plt.bar(categories, values)

plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.grid(axis="y")

plt.show()
