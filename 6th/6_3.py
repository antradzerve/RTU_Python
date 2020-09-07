sentence = input("Enter a sentence  ")
words = sentence.split(" ")

new_sentence = []

for oneWord in words:
    reverseWord = oneWord[::-1]
    new_sentence.append(reverseWord)
    new_sentence_final = " ".join(new_sentence).capitalize()

print(new_sentence_final)