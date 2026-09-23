##Save generated charts as image files inside the project folder.##
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 120, 150, 130, 180]

plt.figure(figsize=(8, 5))

plt.plot(months, sales, marker="o", label="Sales")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)
plt.legend()

plt.savefig("monthly_sales.png")

plt.show()