# Genrate a random Password 


import random

## Greet User

print("Welcome to the Pypassowrd Genrator!")

# Creating a list for numbers, letters and symbols

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '0', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Taking user input 


user_letters = int(input("How many letters would you like in your password?\n"))

user_symbols = int(input("How many symbols would you like in your password?\n"))

user_numbers = int(input("How many numbers would you like in your password?\n"))


# Logic 


list_password = []


for len in range(0,user_letters):
    list_password.append(random.choice(letters))

for num in range(0,user_numbers):
    list_password.append(random.choice(numbers))


for sym in range(0,user_symbols):
    list_password.append(random.choice(symbols))


random.shuffle(list_password)

# converting list in string 

password = ""

for char in list_password:
    password += char



print(f"You new password is =  {password}")

