even_sum=0
odd_sum=0

#Adds even numbers between 0 and 100(inclusive)
for i in range(0,101):
    if i % 2== 0:
        even_sum+=i
print("Sum of all even numbers from 0 to 100 is " + str(even_sum))

#Adds odd numbers between 0 and 100(inclusive)
for i in range(0,101):
    if i%2!=0:
        odd_sum+=i
print("Sum of all odd numbers from 0 to 100 is " + str(odd_sum))
