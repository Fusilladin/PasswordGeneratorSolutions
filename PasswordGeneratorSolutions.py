# PASSWORD GENERATOR SOLUTIONS

import random

x = input('Do you want a strong or a weak password? strong/weak  ')

if x == 'strong':
    a = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    passlen = 12
    p =  "".join(random.sample(a,passlen ))
    print(p)
elif x == 'weak':
    b = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    passlen = 7
    p =  "".join(random.sample(b,passlen ))
    print(p)
else:
    print('Please enter either "strong" or "weak".')
