# 1. Arithmetic operators
# 2. Assignment operators
# 3. Comparison operators
# 4. Logical-Operators

a=10
b=3
#--------------------------------------------------------------------------------------------------------------------------",
# Operator					Shorthand form	What It Does",
# --------------------------------------------------",
# + 	Addition 			+=				Add two operands",
# - 	Subtraction 		-=				Subtract right operand from the left ",
# * 	Multiplication 		*=				Multiply two operands",
# / 	Division 			/=				Divides the operand on left by the one on right.",		 
# % 	Modulus 			%=				Divides the operand on left by the one on right and returns	remainder",
# ** 	Exponent 			**=				left operand raised to the power of right",
# // 	Floor division 		//=				Performs just like the / division operator, but truncates the result at the decimal point",
#--------------------------------------------------------------------------------------------------------------------------",
result=a+b
#print(result)

#print("The addition of "+a+" and "+b+" is "+result)
#print("The addition of "+str(a)+" and "+str(b)+" is "+str(result))
print("The addition of %f and %d is %d" %(a,b,result))

# result=a-b
# print("The substraction of %d and %d is %d" %(a,b,result))

# result=a*b
# print("The multiplication of %d and %d is %d" %(a,b,result))

# result=a/b
# print("The division of %d and %d is %d" %(a,b,result))

# result=a%b
# print("The Modulus of %d and %d is %d" %(a,b,result))

# result=a**b
# print("The Exponent of %d and %d is %d" %(a,b,result))

# result=a//b
# print("The Floor division of %d and %d is %d" %(a,b,result))

# # a+b -->عبارت
# # print(result)-->دستور

c=10
c+=3 #--->c=c+3
c-=1
print(c)
