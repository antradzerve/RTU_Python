a = float(input("Ievadiet pirmo skaitli"))
b = float(input("Ievadiet otro skaitli"))
c = float(input("Ievadiet trešo skaitli"))

if (a>=b and a>=c and b>=c):
  print(f"{c} {b} {a}")
elif (a>=b and a>=c and b<=c):
    print(f"{b} {c} {a}")
elif (a<=b and a>=c and b>=c):
    print(f"{c} {a} {b}")
elif (a<=b and a<=c and b<=c):
    print(f"{a} {b} {c}")
elif (a<=b and a<=c and b>=c):
    print(f"{a} {c} {b}")
else:
    print(f"{b} {a} {c}")