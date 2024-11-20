import random


heads=0
tails=0
for i in range(1000000):
    coin=random.randint(1,2)
    if coin==1:
        tails+=1
    if coin==2:
        heads+=1
print(str(heads) + " Heads")
print(str(tails) + " Tails")
ratio=int(heads) / int(tails)
print("Ratio of heads to tails: ",  round(ratio, 4))
