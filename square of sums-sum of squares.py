sum_of_squares=0
square_of_sums=0
for number in range(1,101,1):
    sum_of_squares+=number**2
    square_of_sums+=number
    
square_of_sums=square_of_sums**2

print(square_of_sums-sum_of_squares)
