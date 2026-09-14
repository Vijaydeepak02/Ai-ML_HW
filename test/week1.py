##week1test##
def check(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

for i in range(5):
    number = int(input("Enter a number: "))
    
    result = check(number)
    print(number, "is", result)