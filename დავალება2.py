#დავალება მეორე
#1
num_list = [44, 23, 11, 8, 20, 56, 33, 55]
number = int(input("Enter a number: "))

if number in num_list:
    print("The number is in the list")
else:
    print("The number is not in the list") 

#2
num1 = int(input("Enter an integer: "))

if num1%2 == 0:
    print("The number is even!")
elif num1%2 == 1:
    print("The number is odd!")

#3
str1 = "Python"
str2 = "Python"

if str1 == str2:
    print("Same object")
else:
    print("Different object")

#4
num_list = [44, 23, 11, 8, 20, 56, 33, 55]
num = int(input("Enter a number: "))

if num_list[3] <= num < num_list[7]:
    print("More than list elements")
elif num == num_list[5]:
    print("Equal")
else:
    print("None of the conditions were met")


