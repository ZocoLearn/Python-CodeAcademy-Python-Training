def is_palindrome(text):
    print(text[::-1].lower())
    return text[::-1].lower()==text.lower()

print(is_palindrome("Dad"))
# is_palindrome("drd")
