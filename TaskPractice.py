# student  Q/A Report Card  TASK PRACTICE

print("\n ---- Welcome to the Student Report Card Generator!----\n")

# print("Please enter the following details to generate the report card:\n")
# print ("Note: Please enter the marks in English subject out of 100.\n")


Name=input("Enter Your Name: ")
Class=input("Enter Your Class: ")
RollNumber=input("Enter Your Roll Number: ")
Marks=input("Enter Your Marks in integers: ")

# get the marks and calculate the grade and print the report card with the details of the student and the grade obtained in English subject. 

print("\n-------------Report Card-------------\n")
print(f" Candidate Name: {Name}")
print(f" Class: {Class}")
print(f" Candidate's Roll Number: {RollNumber}")
print(f" Marks Obtain in English: {Marks}")

# using if-else statement to calculate the grade based on the marks obtained in English subject and print the grade in the report card.

if(int(Marks) >= 90):
    print(" Grade: A")
elif(int(Marks) >= 80):
    print(" Grade: B")
elif(int(Marks) >= 70):
    print(" Grade: C")
elif(int(Marks) >= 60):
    print(" Grade: D")
else:
    print(" Grade: F")

print("\n-------------End of Report Card-------------\n")


