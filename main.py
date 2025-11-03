import time
my_time = int(input("enter the time in seconds"))
for x in range(0,my_time):
    print(f"00:00:{x}")
    time.sleep(1)
print("your time is up")    
     
