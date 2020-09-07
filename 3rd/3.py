for x in range(1,100):
    z=""
    if x%5==0:
        z+="fizz"
    if x%7==0:
        z+="Buzz"
    if z=="":
        z=x   
    
    print(z)