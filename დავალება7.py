#1

set1 = set()

input1 = input("Enter something: ").split()

for i in input1:
    if i.isdigit():      #თუ არის ინტეჯერი მაგას შეამოწმებს
        set1.add(int(i))   
    else:
        set1.add(i)        

print(set1)

#2

set2 = set()

input2 = input("Enter something: ").split()

for k in input2:
    if k.isdigit():     
        set2.add(int(k))   
    else:
        set2.add(k)


set2 = frozenset(set2)

print(set2)

#3

set3 = set()
set4 = set()

in1 = input("Enter Anything: ").split()
in2 = input("Enter Anything: ").split()

for z1 in in1:
    if z1.isdigit():     
        set3.add(int(z1))   
    else:
        set3.add(z1)
        
for z2 in in2:
    if z2.isdigit():     
        set4.add(int(z2))   
    else:
        set4.add(z2)
        
together = set3.union(set4)
together = tuple(together)
print(together)

#4

tuple1 = tuple(input("Enter Anything: ").split())
arr1 = []

for i5 in tuple1:
    for z5 in i5:
        if z5.isdigit():
           arr1.append(int(z5))
        else:
           arr1.append(z5)

print(arr1)


#5

arr3 = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]

for stud in arr3:
    a, b = stud
    print(f"Name: {a}, Age: {b}")

#6

arr4 = ["Irakli", "Giorgi", "Nona", "Oto"]
arr5 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]

arr4 = set(arr4)
arr5 = set(arr5)

intersection = arr4.intersection(arr5)
print(intersection)





    



        


    




