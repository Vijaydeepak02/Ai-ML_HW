##Generate random integers and floats, then inspect the generated values and ranges.##
import numpy as np

random_integers = np.random.randint(1, 101, 10)

random_floats = np.random.rand(10)

print("Random Integers:")
print(random_integers)

print("\nRandom Floats:")
print(random_floats)

print("\nInteger Minimum:", random_integers.min())
print("Integer Maximum:", random_integers.max())

print("\nFloat Minimum:", random_floats.min())
print("Float Maximum:", random_floats.max())