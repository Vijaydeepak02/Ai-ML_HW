##Plot two numerical columns in a scatter plot and observe the relationship between them.##
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6, 7, 8]
marks = [50, 55, 60, 65, 70, 75, 80, 90]

plt.scatter(hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.grid(True)

plt.show()