#Take input for the student that he xan attend the exam or not
medical_cause = input("Did you have a medical cause? If yes press Y and if no press N : ")

#Take input of the attendance
atten = int(input("Enter the attendance percentage of the student : "))

#Checking the user input predicting output accordingly

if medical_cause == 'Y' : #Checking the candition 1
    print("You are allowed to continue classes.")
else:
    if atten>=75: #Checkiing the condition 2
        print("You are allowed to continue classes.")  
    else:
        print("Sorry, you are not allowed to do classes.")      