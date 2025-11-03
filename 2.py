rows = int(input("enter the number of rows:"))
columns = int(input("enter the numbers of columns:"))
symbol = input("enter a symbol to use")
for x in range(rows): 
    for y in range(columns):
        print(symbol,end=" ")
    print()      