treeHeight = int(input("Enter tree height in whole numbers"))

i = 0
while i < treeHeight:
    if i >= 0:
        print(" "*(treeHeight-i) + "*"*(2*i+1))
    i += 1


print("\n")
treeHeight2 = int(input("Enter tree height in whole numbers"))
print("\n")

for n in range(0, treeHeight2):
    if n >= 0:
        print(" "*(treeHeight2-n) + "*"*(2*n+1))