##Write four functions: square, cube, factorial, and simple interest. Call each function with sample inputs.##
def square(n):
    return n * n

def cube(n):
    return n * n * n

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

def simple_interest(p, r, t):
    return (p * r * t) / 100

number = int(input("Enter a number: "))

print("Square:", square(number))
print("Cube:", cube(number))
print("Factorial:", factorial(number))

p = float(input("Enter principal amount: "))
r = float(input("Enter interest rate: "))
t = float(input("Enter time: "))

print("Simple Interest:", simple_interest(p, r, t))