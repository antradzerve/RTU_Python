name = input("Kā Tevi sauc?")

nameBackwards = name[::-1]
lowNameBackwards = nameBackwards.lower().capitalize()

print(f"{lowNameBackwards}, pamatīgs juceklis vai ne, {name[0]}?")