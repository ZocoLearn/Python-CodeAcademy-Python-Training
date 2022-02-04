total_price=int(input("Enter Total Order Price :"))

def validate_free_Shipping(price):
    if price>40:
        print("Correct")
    else:
        print("Not Correct")
validate_free_Shipping(total_price)