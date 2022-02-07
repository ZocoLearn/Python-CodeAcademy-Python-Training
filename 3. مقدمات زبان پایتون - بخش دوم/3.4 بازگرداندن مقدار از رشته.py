
from math import fabs


def sum_numbers(num1,num2):
    return num1+num2
    
sum=sum_numbers(10,20)
print(sum)

#-------------------------------
def is_even(number):
    if number%2==0:
        return True
    else:
        return False

result=is_even(3)
print(result)
#-------------------------------
def is_even2(number):
    result=None
    if number%2==0:
        result= True
    else:
        result= False
    return result

result=is_even2(3)
print(result)