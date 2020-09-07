i = 1
while i < 101:
    if i % 5 == 0 and i % 7 == 0:
        print("FizzBuzz,", end = "")
    elif i % 7 == 0:
        print("Buzz,", end = "")
    elif i % 5 == 0:
        print("Fizz,", end = "")
    else:
        print(i, ",", end = "")
    i += 1