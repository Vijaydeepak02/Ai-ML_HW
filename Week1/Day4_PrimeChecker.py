##Write a function that checks whether a number is prime. Test it with different values.##
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

number = int(input("Enter a number: "))

if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")