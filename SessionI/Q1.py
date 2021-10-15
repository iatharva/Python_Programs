#Write a program to swap two numbers using a third variable

#Accpeting two values
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
#swap two number using third variable
container = number1
number1 = number2
number2 = container
print ("The value of x after swapping: ",number1)
print ("The value of y after swapping: ",number2)
input("Press enter to exit")
