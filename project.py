import string
import random
n = int(input("Default length is 12 characters.Please enter length of password you want."))
pass_character = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation

def org(n):
    password = random.choice(string.digits)+random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.punctuation)

    for i in range(1, n-3):
        s = random.choice(pass_character)
        if s == '<' or s == '>':
            s = random.choice(pass_character)
        password = password+s

    return password

if n < 12:
    p = org(12)
    print(p, 'password generated 12 characters long by default.')
    print("Password length is:", len(p))
else:
    p = org(n)
    print(p)
    print("Password length is:", len(p))
