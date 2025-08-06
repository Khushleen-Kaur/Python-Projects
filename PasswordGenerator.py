import random
import string

AllChar = string.ascii_letters + string.digits + string.punctuation
SomeChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$&*"

length = int(input("Enter length of password : "))
password =''

for i in range(length):
    password = password + random.choice(SomeChar)

print(length , "digit pasword is :" , password)

