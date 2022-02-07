
def secure_card_number(card_number):
    secured="*"*15+card_number[len(card_number)-4:]
    #secured="*************"+card_number[-4:]
    return secured
card_number=input("enter card number:")
print(secure_card_number(card_number))