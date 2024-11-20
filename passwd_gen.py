import random

while True:
    uppercasechar_1 = chr(random.randint(65,90)) #Used to generate a random UPPERCASE Character
    uppercasechar_2 = chr(random.randint(65,90)) #Random Uppercase
    lowercasechar_1 = chr(random.randint(97,122)) #Random Lowercase
    lowercasechar_2 = chr(random.randint(97,122)) #Random Lowercase
    number_1 = chr(random.randint(48,57)) #Random Numerical digit
    number_2 = chr(random.randint(48,57)) #Random Numerical digit
    symbol_1 = chr(random.randint(33,63)) #Random Special character
    symbol_2 = chr(random.randint(33,63)) #Random Special character
    
    salt = "%@*|" + chr(random.randint(33,122)) #Not a true salt, just a basic concept placeholder
    
    password = (uppercasechar_1 + uppercasechar_2 + uppercasechar_1 + uppercasechar_2 + lowercasechar_1 + lowercasechar_2 + number_1 + number_2 + number_1 + number_2 + symbol_1 + symbol_2 + symbol_1 + symbol_2)
    pw_list = list(password + salt)
    random.shuffle(pw_list)
    password = "".join(pw_list)
    print("Look your new password -> " + password + " <-")
    input("\nPress Enter to generate another new password of Ctrl +'c' to close.\n")