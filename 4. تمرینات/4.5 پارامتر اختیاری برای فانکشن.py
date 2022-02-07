
def compare_text(text1,text2,is_case_sensitivecheck=False):
    if not is_case_sensitivecheck:
        return text1.upper()==text2.upper()
    else:
        return text1==text2

print(compare_text("Blank Space","blank space"))

print(compare_text("Blank Space","blank space",True))
