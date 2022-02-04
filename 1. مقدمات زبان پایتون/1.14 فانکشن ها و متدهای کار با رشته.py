#functions(print-input)

#-------------------------------------------------------------------------------------------"
#   String-Functions-Method       			description",
#-------------------------------------------------------------------------------------------"
#   len()               Returns the number of characters in a string",
#   capitalize()        Converts the first character of a string to capital letter",
#   count()             Returns the number of occurrences of a substring in the given string"
#   lower()             Converts a string into lower case",
#   upper()	            Converts a string into upper case",
#   isspace()           Returns True if all characters in the string are whitespaces",
#   replace()           Replaces all or part of a string with another string",
#   isdigit()           Returns True if the string consists of digits only",
#-------------------------------------------------------------------------------------------"

my_name="mohammad   "
result=len(my_name)
# print(result)
# print("%s has %d charecters" %(my_name,result))
# #---------------------
# my_name="mohammad  "
# result=len(my_name)
# print("%s has %d charecters" %(my_name,result))
# #---------------------Method
# result=my_name.capitalize()
# result="ali".capitalize()
# print(result)

# #--------------------------
# quote = """If you really want to do something, you'll find a way.you don't, 
#     you'll find an excuse"""
# sub_string = "you"
# result = quote.count(sub_string)
# print("The substring %s is repeated %d times in the string" %(sub_string,result))
# #--------------------------------
# print("Password".lower())
# print("Password".upper())
# #----------------------------
# print("A  ".isspace())
# print("   ".isspace())
# #-------------------------
# quote = "All progres takes place outside the comfort zone!\""
# quote = quote.replace("progres", "progress1")
# print(quote)
# #---------------------------
print("123456".isdigit())






