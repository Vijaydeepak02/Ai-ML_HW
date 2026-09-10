##Practice string length, uppercase, lowercase, reverse, and vowel count operations. Use separate functions where possible.##
text = input("Enter a string: ")

def find_length(text):
    return len(text)

def make_uppercase(text):
    return text.upper()

def make_lowercase(text):
    return text.lower()

def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

print("Length:", find_length(text))
print("Uppercase:", make_uppercase(text))
print("Lowercase:", make_lowercase(text))
print("Reverse:", reverse_string(text))
print("Vowels:", count_vowels(text))
