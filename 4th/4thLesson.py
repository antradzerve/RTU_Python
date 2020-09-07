i = 0
while i < 5:
    print("Hello", i)
    i+= 1

total = 0
n = 20
while n <= 30:
        total += n
        n += 1
print(total)

while True:
    myInput = input("Enter number or q to quit")
    if myInput =="q":
        break
    num = float(myInput)
    print(num, "cubed is", num**3)

i = 0
while i < 10:
    if i % 2 == 0:
        print("even number", i)
        i+= 1
        continue
    print("generic", i)
    i += 1