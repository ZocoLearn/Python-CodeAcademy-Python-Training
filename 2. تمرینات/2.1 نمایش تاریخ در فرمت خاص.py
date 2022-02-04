from cgitb import reset


def print_date(day,month,year):
    result="%d/%d/%d"%(year,month,day)
    print(result)

print_date(10,12,2020)