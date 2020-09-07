start = int(input("start number"))
end = int(input("end number"))

if end<start:
    (start,end) = (end,start)

numnum = list(range(start,end+1))
cubes_1 = []

for n in numnum:
    cubes_1.append(n*n*n)
    print(f"{n} cubed is {n*n*n}")
print(cubes_1)