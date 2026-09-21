##Create a simple line chart with title, axis labels, and readable formatting.##
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y)

plt.title("Simple Line Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.grid(True)

plt.show()
