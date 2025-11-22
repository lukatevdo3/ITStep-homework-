#1

arr = []

while True:
    
    symbol = input("Please enter a symbol: " )
    
    if symbol == "a":
        arr.append(input("Add anything: "))
        continue
    if symbol == "r":
        arr.remove(input("Remove existing: "))
        continue
    if symbol == "e":
        print(f"Your list is: {arr}")
        break
    else:
        print("None of the symbols were matched")
        break

#2

my_list_1 = [43, '22', 12, 66, 210, ["hi"]]

index_of = my_list_1.index(210)
print(index_of)

my_list_1[5].append("hello")
print(my_list_1)

my_list_1.pop(2)
print(my_list_1)

my_llist_2 = my_list_1
my_llist_2.clear()
print(f"My list : {my_llist_2}")

#3

import re 

number = input("Enter you phone number: ")
pattern = r"\(\d{3}\) \d{3}\-\d{3}"

match = re.fullmatch(pattern, number)

if match == None:
    print("Invalid format")
else:
    print(match)
