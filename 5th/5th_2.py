fullText = input("Ievadi vārdu(s) ")
letter = input("Ievadi vienu burtu ")
length = len(fullText)

comparison = length * letter

newName = ""

for c1, c2 in zip(fullText, comparison):
    if c1 == c2:
        newName += c1  
    elif c1 == " ":
        newName += " "
    else:
        newName += "*"
print(newName)