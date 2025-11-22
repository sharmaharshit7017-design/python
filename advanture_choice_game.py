name = input("enter your name to start as a game character: ")
x= int(0)
while x == 0:
    print(f"\\\\welcome {name} to the choice advanture game////")
    print("You are on a road it has come to end.. You have two options to choose from:\n")
    print("A:press 2 if u wanna go left\nB:press 3 if u wanna go right")
    answer = input("enter your choice: ").lower()
    if answer == "2":
        while True:
            print("you have come near a bridge it looks old can fall anytime you have two options:")
            choice = input("A: press (w) to cross the bridge \nB: press (S) to go back").lower()
            if choice == "w":
                print("bridge fall as you steeped on it and you died unfortunatly..game over look at warning next time")
                print("do you want to play again? y/n").lower()
                if ans == "y":
                    x = 0
                elif ans == "n":
                    x+=1
                    print("thankyou visit again")
                    break
            elif choice =="s":
                print("you went back now you have only right to go")
                print("you have come across river it look deep you have two options:")
            choice = input("A: press (d) to swim across \nB: press(a) to build a raft").lower()
            if choice =="d":
                print(":you swam across the river succesfully and won THANKYOU FOR PLAYING THE GAME")
                break
            elif choice =="a":
                print("your raft broke in the middle and your leg tied with a rope unfortunatly you drowned ... game over")
                break
            else:
                print("invalid choice ")
                break
    elif answer == "3":
        while True:
            print("you have come across river it look deep you have two options:")
            choice = input("A: press (d) to swim across \nB: press(a) to build a raft").lower()
            if choice =="d":
                print(":you swam across the river succesfully and won THANKYOU FOR PLAYING THE GAME")
                ans=input("do you want to play again? y/n").lower()
                if ans == "y":
                    x = 0
                elif ans == "n":
                    x+=1
                    print("thankyou visit again")
                    break
                
                

            elif choice =="a":
                print("your raft broke in the middle and your leg tied with a rope unfortunatly you drowned ...game over")
                ans=input("do you want to play again? y/n").lower()
                if ans == "y":
                    x = 0
                elif ans == "n":
                    x+=1
                    print("thankyou visit again")
                    break

                
            
    else:
        print("invaild choice")
    

    