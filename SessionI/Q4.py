#Write a program to read three numbers and if any two variables are equal, print that number.

#Accepting three numbers
number1 =input("Enter a number: ")
number2 = input("Enter number 2: ")
number3 = input("Enter number 3: ")
#Checking if any two numbers are equal
if number1 == number2 or number1 == number3:
    print(number1," is the value common in at least two variables")
elif  number2 == number3:
    print(number2," is the value common in at least two variables")
else:
    print("None of the values are equal")
