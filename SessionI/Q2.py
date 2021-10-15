#Write a program to swap two numbers without using third variable.

#Accpeting two values from user
number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
print("Before swapping: ",number1,number2) #for example n1=10,n2=20
#swap without using third variable
number1=number1+number2 #n1=10+20=30
number2=number1-number2 #n2=30-20=10
number1=number1-number2 #n1=30-10=20
print("After swapping: ",number1,number2)
