#4 رقم یا 6 رقم و همه آن عدد باشد
def validate_pin_code(pin_code):
    if(pin_code.isdigit()):
        if(len(pin_code)==4 or len(pin_code)==6):
            return True
    return False

print(validate_pin_code("1245"))

print(validate_pin_code("124554"))

print(validate_pin_code("12455"))

print(validate_pin_code("12455a"))
print(validate_pin_code("1245 a"))
