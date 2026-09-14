##Check whether a given word is a palindrome by reversing the text manually.##
word = input("Enter a word: ")

reverse = ""

for char in word:
    reverse = char + reverse

if word == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")