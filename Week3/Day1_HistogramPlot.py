##Create a histogram using random or sample numeric data and experiment with bins.##
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(40, 101, 50)

plt.hist(data, bins=5)

plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.grid(axis="y")

plt.show()
