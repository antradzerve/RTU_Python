for n in range(1,20, 2):
    print(n)

food = "kartupelis"
for c in food:
    print("Letter", c)
    print("\n")

myList = [1,2,3,5,8,94,247,-50]
total = 0
for num in myList:
    print(num)
    total += num
print(total)
print(sum(myList))

record = None
for num in myList:
    if record == None:
        record = num
    if num > record:
        record = num
print("largest is ", record)


otherFood = "potatoes"
for i, p in enumerate(otherFood, start = 1):
    print(f"char no. {i} is {p}")