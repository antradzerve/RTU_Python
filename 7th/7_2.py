sentence = input("Enter text to check if palindrome:  ")

new_sentence = ''.join(sentence.split()).lower()
reverse_NS = new_sentence[::-1]

def palindrome_check(one, two):
    if one == two:
        return True
    return False

print(palindrome_check(new_sentence, reverse_NS))


