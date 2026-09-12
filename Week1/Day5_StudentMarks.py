##Store marks for five students in a dictionary and calculate the average and grade for each student.##
students = {
    "John": [80, 75, 90],
    "Alice": [90, 85, 95],
    "Bob": [70, 65, 75],
    "David": [60, 70, 65],
    "Emma": [85, 80, 90]
}

for name, marks in students.items():
    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print(name, "Average:", average, "Grade:", grade)