userTemperature= float(input("What is your temperature?"))

lowTemp = 35
highTemp = 37

if userTemperature < lowTemp:
  print("Nav par aukstu?")
elif lowTemp<=userTemperature<=highTemp:
  print("Viss kārtībā!")
else:
  print("Iespējams drudzis!")