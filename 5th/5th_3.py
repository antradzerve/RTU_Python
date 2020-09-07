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



