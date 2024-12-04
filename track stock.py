import random
stock=100
print("Value of stock on day 0 is " + str(stock) + " dollars")
for i in range(1,31):
    number=random.randint(1,10)
    if i % 2==0:
        stock+=number
    if i % 2==1:
        stock=stock-number
    print("Value of stock on day " + str(i) + " is " + str(stock) + " dollars")

if stock>100:
    print("You made " + str(stock-100) + " dollars")
elif stock<100:
    print("You lost " + str(stock-100) + " dollars")
elif stock==100:
    print("Stock value is same")
    
