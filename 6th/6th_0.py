myList = [1,2,3,4, "Valaldis"]
needle = "al"

for item in myList:
    if type(item) == str and needle in item:
        print(f"Found {needle=} in {item=}")
    print(item)

myList.append("alus")

find_list = []

for item in myList:
    if type(item) == str and needle in item:
        print(f"Found {needle=} in {item=}")
        find_list.append(item)
print(f"{find_list=}")

new_list = myList + ["Kalejs"]
len(new_list), len(myList)

new_list += ["malejs"]

print(len(new_list), len(myList))
print(new_list)

new_list[-1]
last = new_list.pop()
new_list.append(last)

numbers = [1,2,3,4,4]
sorted(numbers)
numbers.sort()

sentence = "es esmu teksta string"
words = sentence.split( )
new_sentence = " ".join(words)


new_new_list = []
for word in words:
    new_new_list.append(word.capitalize())
print(new_new_list)

new_list_2 = [w.capitalize() for w in words]

# w.startswith("b") same as w[0] == "b"


numnum = list(range(10))
squares = []
for n in numnum:
    squares.append(n*n)

squares_2 = [n*n for n in range(10) if n%2 == 0]

food = "kartupelis"
char_codes = [ord(c) for c in food]

char_codes_list = [[f"Char: {c}", ord(c)] for c in food]
print(char_codes_list[-1][-1])