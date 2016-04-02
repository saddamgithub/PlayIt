# Rolling dice game

import random

print "-- Welcome to Rolling Dice game --"
print "The rules are simple. You roll the dice twice. If you get the same number twice, you win.. Cool right :P Let's get started"

prev_roll = 0

while True:
    print "Press r to roll q to exit"
    inp = raw_input();
    if inp == 'q':
        break

    else if inp == 'r':
        print "Rolling"
        roll = random.randint(1,6)
        if prev_roll != 0 and prev_roll == roll :
            print "You win"
        else:
            print "Try again"
    else:
        print "Invalid entry"
