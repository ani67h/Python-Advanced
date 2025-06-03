# take input from the user
num = int(input("Enter a number : "))
p = int(input("Enter the number of digits : "))

#intialize sum
sum = 0

# find the sum of cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** p
    temp //= 10

# display the result
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")    