#import time
#def count(end,start=0): 
 #   for x in range(end+1,start):
  #      print(x)
   #     time.sleep(1)
    #print("done")
#count(15,17)
def phone(country,area,first,last):
    return f"{  country}-{area}-{first}-{last}"
phone_num=phone(1,123,456,7890)
print(phone_num)