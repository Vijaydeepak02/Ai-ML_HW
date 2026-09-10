##Use a dictionary to count how many times each character appears in a string.##
text = input("Enter a string: ")

count = {}

for char in text:
    if char in count:
        count[char] = count[char] + 1
    else:
        count[char] = 1

print(count)