#Take input from user
rows = int(input("Please enter the total number of rows : "))
number = 1 #intialise by 1

print("Flyod's Triangle")
#outer loop for number of rows
for i in range(1, rows + 1):
    #inner loop for number of columns
      for j in range(1, i+1):
            #display result
              print(number, end = '  ')
              number = number + 1
      print()