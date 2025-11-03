import random
def spin_row():
    symbols =['🍉','🍊','🥭','🍎']
    
    return [random.choice(symbols) for  _ in range(3)]
def print_row(row):
    print("***********")
    print(" ".join(row))
    print("***********")
def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍉':
            return bet*3
        elif row[0] =='🍊':
            return bet*5
        elif row[0]=="🥭":
            return bet*7
        elif row[0]== '🍎':
            return bet*55
    return 0   
        
def main():
    balance =100 
    print("**********************")
    print("welcome to python slot")
    print("symbols::🍉 🍊 🥭 🍎")
    print("**********************")
    while balance >0:
        print(f"current balance:{balance}")
        bet = input("place your bet amount:")

    
        if not bet.isdigit():
            print("please enter a valid number")
            continue
        bet = int(bet) 
        if  bet >balance:
            print("insufficient balance") 
            continue 
        if bet<=0:
            print("bet must be greater  then 0")
            continue
        balance -= bet
        row = spin_row()
        print(row)
        payout = get_payout(row,bet)
        if payout >0:
            print(f'you won{payout}')
        else:
            print("you lost")
        balance+=payout
if __name__=="__main__":
    main()