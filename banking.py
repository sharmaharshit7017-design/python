def show_balance(balance):
    print(f'your balance is{balance}')
def deposite():
    amount =float(input("neter an amount"))
    if amount<0:
        print("that not valid amount")
        return 0
    else:
        return amount
def withdraw(balance):
    amount = float(input("enter the amount"))
    if amount>balance:
        print("insufficient")
    else:
        return amount 
    
def main():
    balance=100
    is_running = True
    while is_running:
        print("banking program")
        print("1.show balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")
        choice=input("enter your choice(1-4):")
        if choice =="1":
            show_balance(balance)
        elif choice=="2":
            balance +=deposite()
        elif choice=="3":
            balance -=withdraw(balance)
        elif choice=='4':
            is_running=False
        else:
            print("that is not valid choice")
        balance -= withdraw
if __name__ == '__main__':
    main()
    