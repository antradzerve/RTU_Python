numberToCheck = int(input("Enter a whole positive number"))

for t in range(2,int(numberToCheck**0.5)+1):
    if numberToCheck % t == 0:
        print("Not a prime")
        break
else:
    print("Prime number!")

    
