
# a=int(input("Please  enter number1 : "))
# b=int(input("Please  enter number1 : "))

# result=a/b
# print(result)

# try:
#     a=int(input("Please  neter number1 : "))
#     b=int(input("Please  neter number1 : "))
# except:
#     print('Somthing went wrong!')
# else:
#     result=a/b
#     print(result)

# try:
#     a=int(input("Please  neter number1 : "))
#     b=int(input("Please  neter number2 : "))
#     if b==0:
#         print('Somthing went wrong!')
#     else:
#         result=a/b
    
# except:
#     print('Somthing went wrong!')
# else:
#     print(result)


#----------------
try:
    a=int(input("Please  neter number1 : "))
    b=int(input("Please  neter number1 : "))
    result=a/b
    
except:
    print('Somthing went wrong!')
else:
    print(result)
finally:
    # if socket.status=="open":
    #     socket.close()
    print("Finally Part")

    