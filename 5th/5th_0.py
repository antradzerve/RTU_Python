#1st task

name = input("Kā Tevi sauc?")

nameBackwards = name[::-1]
lowNameBackwards = nameBackwards.lower().capitalize()

print(f"{lowNameBackwards}, pamatīgs juceklis vai ne, {name[0]}?")


#2nd task

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


#3rd task

inputText = input("Lūdzu, ievadi tekstu! ")

word1 = "nav"
word2 = "slikt"

word1Find = inputText.find(word1)
word2Find = inputText.rfind(word2) + len(word2)

positiveText = inputText[:word1Find] +"ir lab" + inputText[word2Find:]

if word1Find != -1 and word2Find != -1:
    print(positiveText)
else:
   print(inputText)



