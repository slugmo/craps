from random import randint

print('come-out')
r1 = randint(1, 6) #r1 is not a meaningful variable name. What does 1 and 6 mean
r2 = randint(1, 6) #r2 is not a meaningful variable name. what does 1 and 6 mean
v = r1 + r2 #v is not a meaningful variable name
print(v)
if v == 7 or v == 11: #What does 7 or 11 mean?
    print('You win!')
elif v == 2 or v == 3 or v == 12: # What does 2, 3 or 12 mean
    print('Craps, you lose.')
else:
    print('The point is', v)
    r1 = randint(1, 6) #What does r1, 1 or 6 mean
    r2 = randint(1, 6) #What does r2 mean
    w = r1 + r2 # W is not a meaningful variable name
    print(w)
    while w != v and w != 7: #What does w, v, or 7 mean
        r1 = randint(1, 6)
        r2 = randint(1, 6)
        w = r1 + r2
        print(w)
    if w == 7:
        print('Seven out, you lose.')
    else:
        print('Pass, you win!')
