import random
gen_number=random.randint(1,100)
guess=int(input("Guess a number 1 through 100 and I'll tell you if it's too high, low, or if you got it!"))
while guess!=gen_number:
    
    if guess<gen_number:
        print("Too low!")
    elif guess>gen_number:
        print("Too high!")
    guess=int(input("Guess a number 1 through 100 and I'll tell you if it's too high, low, or if you got it!"))

if guess==gen_number:
    print("You got it! The number was " + str(gen_number))
