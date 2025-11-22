import random
max_lines = 3
max_bet = 100
min_bet = 1
rows = 3
cols = 3
symbol_count = {
    'A':5,
    'B':4,
    'C':3,
    'D':2
}
def slot_machine(rows,cols,symbols):
    all_symbols =[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns =[]
    for col in range (cols):
        column =[]
        current_symbols = all_symbols[:]
        for row in range (rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposite():
    while True:
        amount = input("enter deposite amount:")
        if amount.isdigit():
            amount = int(amount)
            if amount >0:                
                break
            else:
                print("amount must be greater than 0")
        else:
            print("please enter a valid amount")
    return amount
def get_number_of_lines():
    while True:
        lines = input(f"enter number of lines to bet on (1-{max_lines}):")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= max_lines:
                break
            else:
                print("enter a valid number of lines")
        else:
            print("please enter a number")
    return lines
def get_bet():
    while True:
        bet = input(f"enter bet amount per line (1-{max_bet}):")
        if bet.isdigit():
            bet = int(bet)
            if 1 <= bet <= max_bet:
                break
            else:
                print(f"bet must be between 1 and {max_bet}")
        else:
            print("please enter a valid bet amount")
    return bet
def main():
    balance = deposite()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"insufficient balance. your current balance is {balance}")
        else:
            break
    print(balance,lines) 
    total_bet = bet * lines
    print(f"you are betting {bet} on {lines} lines. total bet is {total_bet}")
main()



            
        