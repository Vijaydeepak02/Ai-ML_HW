##Generate the Fibonacci series for N terms using loops and add comments explaining the logic.##
n = int(input("Enter the number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    c = a + b

    a = b
    b = c