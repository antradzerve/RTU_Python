# myFood = "potatoes"
myFood = input("What is your favourite food?")

# price = 0.45
price = float(input(f"How much does {myFood} cost in your shop?"))

#quantity = 10

quantity = int(input(f"How many pieces of {myFood} do you want?"))

total = round(price*quantity, 2)
print(f"It will cost {total} to buy {quantity} kg of {myFood}")