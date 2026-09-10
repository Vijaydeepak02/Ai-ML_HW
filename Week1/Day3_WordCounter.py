##Read a sentence, count the number of words, and print the length of each word.##
sentence = input("Enter a sentence: ")

words = sentence.split()

print("Number of words:", len(words))

for word in words:
    print(word, len(word))