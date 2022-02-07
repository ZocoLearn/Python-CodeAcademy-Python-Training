from unicodedata import name


def get_user_info():
    name=input("enter your name:")
    age=input("enter your age:")
    return name,age

user_name,user_age=get_user_info()
print(user_name)
print(user_age)