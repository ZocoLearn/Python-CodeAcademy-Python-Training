# 1. Arithmetic operators
# 2. Assignment operators
# 3. Comparison operators
# 4. Logical-Operators

# if condition:
#     block

from math import fabs
from operator import truediv


speed=120

if speed>100:
    print("You drive fast")

if speed>50:
    ghjsghf
    hsgfhgs
    hsgfhsf



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
elif speed>120:
    print("You dont drive fast") 
elif speed==140:
    print("speed=140")
elif speed!=140:
    print("speed!=140")
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

is_marrid=False

if is_marrid==True:
    print("fssfs")
if is_marrid:
    print("fssfs")


if  is_marrid==False:
    print("fssfs")
if not is_marrid:
    print("fssfs")

