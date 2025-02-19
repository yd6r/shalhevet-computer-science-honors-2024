"""
 Write a program that guesses every possible 4 digit passcode
 combinations until the correct passcode is guessed.

 The passcode is randomly generated and stored in the variable
 secretPasscode.

 Print out how many guesses it took to guess the correct passcode.
"""
import random

# Checks whether the given guess passcode is the correct passcode
def is_correct(guess_code, correct_code):
    return guess_code == correct_code

# Generates a random 4 digit passcode and returns it as a String
def generate_random_passcode():
    random_passcode = ""
    
    for i in range(4):
        random_digit = random.randint(0, 9)
        random_passcode += str(random_digit)
    return random_passcode

secret_passcode = generate_random_passcode()
# Checks the maximum amount of numbers possible and then returns the attempts to guess and the code

def guess_passcode():
    new_guess_code=""
    count=0
    for i in range(0,10):
        for x in range(0,10):
            for y in range(0,10):
                for z in range(0,10):
                    count+=1
                    new_guess_code= str(i)+str(x)+str(y)+str(z)
                    if is_correct(new_guess_code, secret_passcode):  
                        print("The code was " + str(secret_passcode))
                        print("It took " + str(count) + " tries to guess the passcode. ")
                        return
guess_passcode()
