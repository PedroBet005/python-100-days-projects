import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=',
    '+', '[', ']', '{', '}', ';', ':', "'", '"', ',', '.', '<', '>',
    '/', '?', '\\', '|', '~', '`'
]

print("Welcome to the password generator")


#Se solicita datos del usuario.

nr_letters = int(input(
    "How many letters do you want your password to have?\n"
))
nr_numbers = int(input(
    "How many numbers do you want your password to have?\n"
))
nr_symbols = int(input(
    "How many symbols do you want your password to have?\n"
))


#Se crea variable, para almacenar datos generados aleatoriamente.
password_list = []

for _ in range(nr_letters):
    password_list.append(random.choice(letters))

for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))


#Se crean 2 print, para ver la diferencia al utilizar shuffle

print(password_list)

random.shuffle(password_list)

print(password_list)


#Se crea variable para almacenar datos generados en la variable contraseña_lista

password = ""

for character in password_list:
    password += character

print(f"The password is: {password}")
