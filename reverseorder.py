#input number grater than 1
n = int(input("Enter the value of n : "))

#print the number from n to 1
print("Numbers from {0} to {1} are: ".format(n,1))

#loop to print numbers
for i in range(n,0,-1):
    print(i)