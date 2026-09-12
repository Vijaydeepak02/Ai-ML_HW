##Create a text file and practice write, append, and read operations using safe file handling methods.##
file = open("sample.txt", "w")
file.write("Hello, this is my first file.")
file.close()

file = open("sample.txt", "a")
file.write("\nThis is an appended line.")
file.close()

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()