
number1=int(input("Enter number1 :"))
number2=int(input("Enter number2 :"))
number3=int(input("Enter number3 :"))


def print_maximum(num1,num2,num3):
    maximum=max(num1,num2,num3)
    print("maxmim between %d and %d and %d is %d"%(num1,num2,num3,maximum))

print_maximum(number1,number2,number3)


def print_maximum_type2(num1,num2,num3):
    if num1>num2 and num1>num3:
        max=num1
    elif num2>num1 and num2>num3:
        max=num2
    else:
        max=num3
    print("maxmim between %d and %d and %d is %d"%(num1,num2,num3,max))

print_maximum_type2(number1,number2,number3)