
def calculate_basic_math(num1,operator,num2):
    if operator=="+":
        result=num1+num2
    elif operator=="-":
        result=num1-num2
    elif operator=="*":
        result=num1*num2
    elif operator=="/":
        result=num1/num2
    else:
        result="operation is not correct"
    print(result)
try:
    num1=int(input("Enter number1 : "))
    operator=input("Enter operator(+ - * / ):")
    num2=int(input("Enter number2 : "))
    
except:
    print("Somthing went wrong")
else:
    calculate_basic_math(num1,operator,num2)
finally:
    print("Completed")
