   #---TASK 3---#

print("COD-SOFT")

import random
import string

def generate_password():
    print("Password Generator")
    length = int(input("Enter password length(min 4): "))
    if length < 4:
        print("Password too short.Please choose atleast 4 charachters.")
        return
    
    charchters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(charchters) for _ in range(length))
    print("Your secure password is: ",password)

generate_password()