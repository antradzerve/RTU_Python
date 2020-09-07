userWorkTime= int(input("Kāds ir Jūsu darba stāžs pilnos gados?"))
userSalary= float(input("Kāda ir Jūsu alga?"))

bonusCash = (userWorkTime - 2) * userSalary * 0.15

if userWorkTime <= 2:
  print("Atvainojiet, bonusu izmaksā tikai tad, ja darba stāžs ir virs 2 pilniem gadiem!")
else:
    print(f"Jums pienākas {bonusCash} eiro liels bonuss.")