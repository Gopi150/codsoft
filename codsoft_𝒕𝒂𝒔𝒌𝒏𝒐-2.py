import random
import string
def passgen(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def checklen():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive length.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def passworgen():
    print("Welcome to the Password Generator")
    len = checklen()
    password = passgen(len)
    print("Generated Password:", password)

passworgen()