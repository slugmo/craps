from random import randint

print('come-out')
dice1 = randint(1, 6) 
dice2 = randint(1, 6) 
comeOutRoll = dice1 + dice2 
print(comeOutRoll)
if comeOutRoll == 7 or comeOutRoll == 11: 
    print('You win!')
elif comeOutRoll == 2 or comeOutRoll == 3 or comeOutRoll == 12: 
    print('Craps, you lose.')
else:
    print('The point is', comeOutRoll)
    dice1 = randint(1, 6) 
    dice2 = randint(1, 6) 
    normalRoll = dice1 + dice2 
    print(normalRoll)
    while normalRoll != comeOutRoll and normalRoll != 7: 
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        normalRoll = dice1 + dice2
        print(w)
    if normalRoll == 7:
        print('Seven out, you lose.')
    else:
        print('Pass, you win!')
