from re import sub


my_list=[10,"Iran",2.1]
# print(my_list)
# print(my_list[2])

# for item in my_list:
#     print(item)

#------------------------------
if "Iran" in my_list:
    print("exist")

#-----------------------
# sub_list=my_list[2:3]
# print(sub_list)
#--------
# sub_list=my_list[-2]
# print(sub_list)
#--------
print(len(my_list))

#--------------
# my_list2=[]
# my_list2.append(1)
# my_list2.append("ali")
# print(my_list2)

#-----------------
# list_1=[1,2,3]
# list_2=[list_1,4,5]
# print(list_2)

#--------
list_1=[10,2,0,30]
list_1[2]=100
print(list_1)
