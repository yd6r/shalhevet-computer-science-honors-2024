import random


times_rolled=0
finished=False

while not finished:
    roll_one=0
    roll_two=0
    roll_three=0
    roll_four=0
    roll_five=0
    times_rolled+=1
    for i in range(1,11):
        roll=random.randint(1,5)
        if roll==1:
            roll_one+=1
        elif roll==2:
            roll_two+=1
        elif roll==3:
            roll_three+=1
        elif roll==4:
            roll_four+=1
        elif roll==5:
            roll_five+=1

    if roll_one==2 and roll_two==2 and roll_three==2 and roll_four==2 and roll_five==2:
        finished=True
print(times_rolled)
