##Solve three short problems that combine concepts from the previous four days.##
numbers = [10, 15, 20, 7, 8]

for number in numbers:
    if number % 2 == 0:
        print(number, "Even")
    else:
        print(number, "Odd")

text = input("Enter a string: ")

count = {}

for char in text:
    count[char] = count.get(char, 0) + 1

print(count)

students = {
    "John": [80, 90, 70],
    "Alice": [90, 85, 95],
    "Bob": [60, 70, 65]
}

for name, marks in students.items():
    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    else:
        grade = "D"

    print(name, "Average:", average, "Grade:", grade)