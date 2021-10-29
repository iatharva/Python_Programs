#Write a program to read three numbers and find smallest of the three.

#Accept three numbers from user
number1 = input("Enter first number: ")
number2 = input("Enter second number: ")
number3 = input("Enter third number: ")
#Find the smallest of the three numbers
if number1 < number2 and number1 < number3:
    print (number1," is the smallest of the three");
elif number2 < number1 and number2 < number3:
    print (number2," is the smallest of the three");
else:
    print (number3," is the smallest of the three");
