import random
low =1
high =100
#options =("rock","paper","scissors")
#cards =["2","3","4","5","k","a","Q"]
#options=random.choice(options) 
number = random.randint(low,high)
#random.shuffle(cards)
#print(cards)
guesses=0
is_running=True
print("python number guessing game")
print(f"select a number{low}and{high}")
while is_running:
    guess =input("enter your guess:")
    if guess.isdigit():
        if guess<low or guess>high:
            print("the number is out of range") 
        
        
    else:
        print("invalid guess")
        print(f"please select a number between{low}and{high}")