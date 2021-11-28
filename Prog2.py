# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex.
# input: P@ssw0rd+P@ssw0rd
# output: Valid
# Tip: loop through each character of the input then process it letter by letter

#Step1 
VPassword = input("Please enter your \33[32m\33[1mPASSWORD\33[0m : ") #Ask for the password

#Step2
num_character = len(VPassword)
specialC, lower, upper, digit = 0, 0, 0, 0

if (len(VPassword) >= 15):
    for me in VPassword:
        if (me.isdigit()):
            digit += 1
        if (me.islower()):
            lower += 1
        if (me.isupper()):
            upper += 1
        if (me == "#" or me == "@" or me == "=" or me == "!" or me == "$" or me == "&" or me == "%" or me == "'" or me == "*" or me == "()" or me == "+ " or me == "." \
        or me == """|""" or me == """^""" or me == "{" or me == "}" or me == "[" or me == "]" or me == "_" or me == "~" or me == "," or me == "?" or me == """+"""):
            specialC += 1

    if (lower >= 1 and upper >= 1 and specialC >= 1 and digit >= 1):
                print("Your \33[32m\33[1mPASSWORD\33[0m is \33[1m\33[95mVALID\33[0m!")  
    if (digit < 1 ):
        print ("Oh no ! Your password must have \33[96m\33[1m\33[3matleast one number.\33[0m")
    if (upper < 1):
        print ("Oh no! Your password must have \33[96m\33[1m\33[3matleast one capital letter.\33[0m")    
    if (specialC < 1):
        print("Oh no! Your password must have \33[96m\33[1m\33[3matleast one special character.\33[0m")
    if (lower <= 1 and upper <= 1 and specialC <=1 and digit <= 1):
        print("Sorry! The \33[32m\33[1mPASSWORD\33[0m you have entered is \33[31m\33[1mINVALID\33[0m❌")
else:
    for me in VPassword:
        if (me.isdigit()):
            digit += 1
        if (me.islower()):
            lower += 1
        if (me.isupper()):
            upper += 1
        if (me == "#" or me == "@" or me == "=" or me == "!" or me == "$" or me == "&" or me == "%" or me == "'" or me == "*" or me == "()" or me == "+ " or me == "." \
        or me == """|""" or me == """^""" or me == "{" or me == "}" or me == "[" or me == "]" or me == "_" or me == "~" or me == "," or me == "?" or me == """+""" ):
            specialC += 1

    print ("Oh no! Your password must have \33[96m\33[1m\33[3matleast fifteen characters.\33[0m")
    if (digit < 1):
        print ("Oh no! Your password must have \33[96m\33[1m\33[3matleast one number.\33[0m")
    if (upper < 1):
        print ("Oh no! Your password must have \33[96m\33[1m\33[3matleast one capital letter.\33[0m")
    if (specialC < 1):
        print("Oh no! Your password must have \33[96m\33[1m\33[3matleast one special character.\33[0m")

    print("Sorry! The \33[32m\33[1mPASSWORD\33[0m you have entered is \33[31m\33[1mINVALID\33[0m❌")


        
