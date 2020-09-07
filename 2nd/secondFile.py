myName = "Antra"
print(f"My name is {myName}")
print(type(myName))

# myName = 5
# print(f"My name is {myName}")
# print(type(myName))
#comments are from ctrl+forward-slash

mySpeed = 90
print(myName + str(mySpeed))

#mySpeed = str(mySpeed) <- this is type casting

pi = 3.14159
print(pi, type(pi))


#mainīgo vērtību maiņa 1
a = 10
b = 20

tmp = a
a = b
b = tmp
print(a, b)

#mainīgo vērtību maiņa 2
a, b = b, a
print(a, b)

print(True, False, type(True))

#typical Boolean values have "is" in front of it - e.g. isSkyBLue

#help("keywords")

print(type(None))

myList = [1,2,-345,"text"]
myDictionary = {'key':'value', 'atslega':'vertiba'}
myTuple = (1,2,None,"Bac",2.3) #fixed values
mySet = {1,1,3,5,6,6,2,9}

print(type(myList), myList)
print(type(myTuple), myTuple)
print(type(mySet), mySet)
print(type(myDictionary), myDictionary.items())