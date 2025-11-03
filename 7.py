menu ={"pizza":3.00,
       "nachos":4.50,
       "popcorn":6.00,
       "fries":2.50,
       "chips":1.00,
       "pretzel":3.50,
       "soda":3.00}
cart=[]
total = 0
for key,value in menu.items():
    print(f"{key}:{value}")
food = input("select an item (q to quit)").lower()
while True:
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
# for food in cart:
#     total += menu.get(food)
#     print(food,end="")