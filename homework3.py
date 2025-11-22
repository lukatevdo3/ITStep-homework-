#1
sum = 0

for i in range(1, eval(input("Please Enter a Number: "))+1):
    sum += i

print(sum)

#2

num = eval(input("\nEnter a Number Larger Than 0: "))

if num >= 0:
    while num > 0:
       print(num, end = " ")
       num -= 1
else:
   print("Enter a number higher than 0! ")

#3 

from random import randint

num1 = randint(1, 100)
i = 1
print("\nLets have a game of guessing. Guess a number between 1 and 100 ... ")

while True:
    guess = eval(input(f"Guess #{i} : "))

    if guess > num1:
        print("Your Number is too great!")
    elif guess < num1:
        print ("Your Number is too little!")
    elif guess == num1:
        print(f"Boolseye! {num1}")
        break
    
    i += 1

#4

total_sum = 0

print("\nAdd numbers to calculate the total sum of yours... ")

while True:
    number = input("Add a number: ")
    
    if number == "sum":
        print(f"Total Sum is : {total_sum}")
        break
    elif eval(number) < 0:
        print("Please Enter a Positive Number!")
    elif eval(number) > 0:
        total_sum += eval(number)
    