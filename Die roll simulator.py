import random
rolled_1=0
rolled_2=0
rolled_3=0
rolled_4=0
rolled_5=0
rolled_6=0
rolled_7=0
rolled_8=0
rolled_9=0
rolled_10=0
rolled_11=0
rolled_12=0
impossible=[1,2,3,4,5,6]

for i in range(100):
    int_1=random.randint(1,12)
    int_2=random.randint(1,12)
    if int_1+int_2==1:
        rolled_1+=1
    if int_1+int_2==2:
        rolled_2+=1
    if int_1+int_2==3:
        rolled_3+=1
    if int_1+int_2==4:
        rolled_4+=1
    if int_1+int_2==5:
        rolled_5+=1
    if int_1+int_2==6:
        rolled_6+=1
    if int_1+int_2==7:
        rolled_7+=1
    if int_1+int_2==8:
        rolled_8+=1
    if int_1+int_2==9:
        rolled_9+=1
    if int_1+int_2==10:
        rolled_10+=1    
    if int_1+int_2==11:
        rolled_11+=1    
    if int_1+int_2==12:
        rolled_12+=1
    
        
print("Rolled ones " + str(rolled_1) + " times")
print("Rolled twos " + str(rolled_2) + " times")
print("Rolled threes " + str(rolled_3) + " times")
print("Rolled fours " + str(rolled_4) + " times")
print("Rolled fives " + str(rolled_5) + " times")
print("Rolled sixes " + str(rolled_6) + " times")
print("Rolled sevens " + str(rolled_7) + " times")
print("Rolled eights " + str(rolled_8) + " times")
print("Rolled nines " + str(rolled_9) + " times")
print("Rolled tens " + str(rolled_10) + " times")
print("Rolled elevens " + str(rolled_11) + " times")
print("Rolled twelves " + str(rolled_12) + " times")

