import random

charStore = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"

passwordLen = int(input("Enter the required password length: "))
passwordCount = int(input("Enter the number of required passwords: "))

for i in range(0, passwordCount):
    password = ""
    for j in range(passwordLen):
        passwordChar = random.choice(charStore)
        password = password + passwordChar
    print(f"Password: {password}")
