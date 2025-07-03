num  = int(input("Enter a number : "))

count = 0
digit = num 

while digit > 0:
    digit = digit // 10
    count += 1

print("There are ",count, "in the number")    