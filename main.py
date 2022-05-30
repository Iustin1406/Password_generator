import random
characters = "abcdefghijklmnopqrstuvwxyz"
upperletters = "ABCEDFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!\"@#$%^&*()-_+{}|\'"
length = int(input("Select password's length : "))
number = int(input("Select de number of generated passwords : "))

want_upperletters = input("Would you like to have upperletters : 'yes' or 'no' ? ")
if want_upperletters == 'yes':
    characters += upperletters

want_digits = input("Would you like to have digits : 'yes' or 'no' ? ")
if want_digits == 'yes':
    characters += digits

want_symbols = input("Would you like to have symbols : 'yes' or 'no' ? ")
if want_symbols == 'yes':
    characters += symbols
for i in range(number):
    password = ""
    for j in range(length):
        password += random.choice(characters)
    print(f'Password with no {i+1} : {password}')
