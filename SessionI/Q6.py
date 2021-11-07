#Write a program to read three number and print them in ascending order (without using sort function)

numbers = []
for i in range(3):
    numbers.append(int(input("Enter a number: ")))
#Sort in ascending order without using sort function
for i in range(3):
    for j in range(i, 3):
        if numbers[i] > numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp
print("Ascending order: ",numbers)
