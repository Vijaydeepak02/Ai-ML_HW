def find_marks(marks):
    p = []
    for mark in marks:
        if mark>35:
            p.append(mark)

    return p

name = input("enter student name: ")

marks = [30,45,82,28,97]

pass_marks = find_marks(marks)

avg = sum(marks)/len(marks)

reverse = name[::-1]

print(name)
print(marks)
print(pass_marks)
print(avg)
print(reverse)