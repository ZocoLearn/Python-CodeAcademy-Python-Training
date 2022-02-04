zip_code=input("Enter Number: ")

def validate_zip_code(num):
    if num.isdigit() and len(num)==5:
        print("%s is correct"%(num))
    else:
        print("%s is not correct"%num)
validate_zip_code(zip_code)   