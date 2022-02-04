# 1. Arithmetic operators
# 2. Assignment operators
# 3. Comparison operators
# 4. Logical-Operators

# if condition:
#     block

speed=120

if speed>100:
    print("You drive fast")


#----------------------------------------------------------------------------------------------------------------------------------",
#  Operator	Operator Name					Description",
#----------------------------------------------------------",
#  == 		Equal to						Returns true if values of both the operands are equal",
#  != 		Not Equal to 					Returns true if values of both the operands are not equal",
#  > 		Greater than 					Returns true if value of the left operand is greater than the right one",
#  < 		Lesser than 					Returns true if value of the left operand is smaller than the right one",
#  >= 		Greater than or equal to 		Returns true if value of the left operand is greater than or equal to the right one",
#  <= 		Less than or equal to			Returns true if value of the left operand is smaller than or equal to the right one",
#----------------------------------------------------------------------------------------------------------------------------------",


if speed>=100 and speed<=120:
    print("You drive fast")

if speed<=100 or speed>=120:
    print("You drive fast")

if speed>=100 and speed<=120:
    print("You drive fast")    
elif speed>12:
    print("You dont drive fast") 
else:
    print("other") 

#-------------------------------------------------------------------------------------"
#  Logical-Operators	    Operator Name		Description",
#-------------------------------------------------------------------------------------"
#  and 		    Logical AND			Returns true when both operands are True",
#  or 		    Logical OR 			Returns true when any one of both operand is True"
#  not 		    Logical NOT 		Reverses the operand state",
#-------------------------------------------------------------------------------------"

if not speed>100:
    print("you drive fast")

