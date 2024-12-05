for i in range(1000):
    hundreds=i//100
    remainder=i%100
    tens=remainder//10
    ones=remainder%10
    if i==hundreds**3 + tens**3 + ones**3:
        print(str(i) + " is an Armstrong number")
