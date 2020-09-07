sentence = input("Enter text to check if palindrome:  ")

def palindrome_check(sentence):
    one = ''.join(sentence.split()).lower()
    two = one[::-1]
    return one == two

print(palindrome_check(sentence))


