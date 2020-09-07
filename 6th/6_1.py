averageList = []

while True:
    myInput = input("Enter number or q to quit ")
    if myInput =="q":
        break
    else:
        num = float(myInput)
        averageList.append(num)
        average = sum(averageList)/len(averageList)
        print(average)
        print(averageList)

        topThree = sorted(averageList)[-3:]
        print(sorted(topThree, reverse=True))
        bottomThree = sorted(averageList)[:3]
        print(bottomThree)
 