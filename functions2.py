#def name(first,last):
 #   first=first.upper()
  #  last=last.upper()
   # return first+" "+last
#full_name = name("harshit","sharma")
#print(full_name)
def net_price(list_price,discount,tax):
    return list_price*(1-discount)*(1+tax)
print(net_price(500,0,0.05))