import random

print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like ?\n"))
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
# Shuffle the list in place
random.shuffle(password_list)
# Create a shuffled password string by joining the list of
# characters ( Delete -> " [] " , " , " and " '' ")
# from ['a', 'b', 'c', 'd'] to abcd
shuffled_password = ''.join(password_list)
print("Here is your password: {}".format(shuffled_password))
