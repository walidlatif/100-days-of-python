import random

print("Customize your password!")
password_lenght = int(input("Choose Password Length : "))
print("Select Password Format :")
print("1 - Easy to say (Avoid numbers and special characters)")
print("2 - Easy to read (Avoid ambiguous characters like l, 1, O, and 0)")
print("3 - All characters (Any character combinations like !, 7, h, K, and l1)")
password_format = int(input())
if password_format == 1:
    print("Select Uppercase, Lowercase, or Both")
    print("1 - Uppercase")
    print("2 - Lowercase")
    print("3 - Uppercase & Lowercase")
    uplow_format = int(input())
    if uplow_format == 1:
        print("#Uppercase")
    elif uplow_format == 2:
        print("#Lowercase")
    elif uplow_format == 3:
        print("#Uppercase & Lowercase")
elif password_format == 2:
    print("Select Uppercase, Lowercase, Numbers, Symbols,  or All")
    print("1 - Uppercase")
    print("2 - Lowercase")
    print("3 - Numbers")
    print("4 - Symbols")
    print("5 - Uppercase & Lowercase.")
    uplow_format = int(input())
    if uplow_format == 1:
        print("#Uppercase")
    elif uplow_format == 2:
        print("#Lowercase")
    elif uplow_format == 3:
        print("#Numbers")
    elif uplow_format == 4:
        print("#Symbols")
    elif uplow_format == 5:
        print("#Uppercase, Lowercase, Numbers, Symbols")
elif password_format == 3:
    print("All characters ")




























'''
symbols = int(input("How many symbols would you like ?\n"))
numbers = int(input("How many number would you like ?\n"))

letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbol = "&*@$%#!?-+_=><|~/\\/{[]}():;,.\"'"
number = "0123456789"
_password = ""

for _ in range(letters):
    le = random.choice(letter)
    _password += le
for _ in range(symbols):
    s = random.choice(symbol)
    _password += s
for _ in range(numbers):
    n = random.choice(number)
    _password += n

password_list = list(_password)
random.shuffle(password_list)
shuffled_password = ''.join(password_list)
print("Here is your password: {}".format(shuffled_password))
'''