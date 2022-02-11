from logging.config import valid_ident
from multiprocessing.sharedctypes import Value


max=0
while True:
    value=input("enter number:")
    if value=="stop":
        break
    else:
        num=int(value)
        if num>max:
            max=num

print("max :%d"%(max))