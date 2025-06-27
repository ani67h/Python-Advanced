num = int(input("Enter a number : "))
pow = int(input("Enter the power : "))

result = 1
i = 1 
while i<=pow:
    result = result * num
    i = i+1

print("\nThe result is = ",result)    