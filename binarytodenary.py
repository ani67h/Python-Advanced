denary = int(input("Enter a number to convert it into Binary number : "))
one = "1"
zero = "0"

for denary in range(zero, one):
   if denary > 1:
       if (denary % 2) == 0:
            print(zero)
        else:
           print(one)      
    else:
       print(one)