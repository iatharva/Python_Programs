#Write a program to read number, if it is even number, print the square of number and if it odd number, print the cube of number.
num=int(input("Enter a number: "))
if num%2==0:
    print(num**2)
else:
    print(num**3)
