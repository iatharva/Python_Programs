#Write a program to count the number of character(character frequency) in a string.
InputString = input("Enter a string: ")
CharCount = {}
for char in InputString:
    if char in CharCount:
        CharCount[char] += 1
    else:
        CharCount[char] = 1
for char, count in CharCount.items():
    print("character {} : {} times".format(char, count))