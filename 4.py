foods =[]
prices = []
while True:
    food=input("enter the food u want to buy(q to quit):")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"enter the price of a {food}:$"))
        foods.append(food)
        prices.append(price)
for x in foods:
    print(x)      

