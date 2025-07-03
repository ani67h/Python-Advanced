denary = int(input("Enter a denary number to know it's binary value : "))
store = ""

while(denary>0):
    binary_value = denary % 2
    store = str(binary_value) + store
    denary = denary//2

print("The binary value is ",store) 

# A bit of this code is taken from youtube videos