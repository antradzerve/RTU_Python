text = 'The quick brown fox jumps over the lazy dog'

def is_pangram(mytext, a='abcdefghijklmnopqrstuvwxyz'):
    
    textual = ''.join(mytext.split()).lower()
        
    return set(textual) == set(a)


isit = is_pangram(text)
print(isit)