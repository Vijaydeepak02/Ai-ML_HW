##Check whether a given word is a palindrome by reversing the text manually.##
word = input("Enter a word: ")

reverse = ""

for i in range(len(word) - 1, -1, -1):
    reverse = reverse + word[i]

print("Reverse:", reverse)

if word == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")