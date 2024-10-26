import random

simbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

count = int(input("Введите длинну пароля"))

password = ""

for i in range(count):
    password = password + random.choice(simbols)

print(password)
