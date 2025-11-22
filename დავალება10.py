import functools
from time import sleep

#1

def func(arr1, arr2):

    zipped = list(str(i) for i in zip(arr1, arr2))

    return zipped



lst1 = list(int(x) for x in input("Enter sequence of numbers: ").split())
lst2 = input("Enter characters: ").split()

print(func(lst1, lst2))

#2

try:
    lst3 = list(int(x) for x in input("Enter Sequence of Numbers: ").split())

    sum1 = functools.reduce(lambda a, b: a*b, lst3)
except TypeError:
    print("Wrong Type of Input!")
except ValueError:
    print("Please Enter Only Numbers!")
else:
    sleep(1)
    print(sum1)
finally:
    print("Process finished!")

#3

try:
    lst4 = list(int(x) for x in input("Enter Sequence of Numbers: ").split())
    filtered = list(filter(lambda x: x%2 == 1, lst4))
    sleep(1)
except ValueError:
    print("Enter only numbers!")
else:
    print(filtered)

#4

try:
    lst5 = input("Enter Sequence of Words: ").split()
    word = input("Enter Ending to match: ")
    filtered1 = list(filter(lambda x: x.endswith(word), lst5))
except TypeError:
    print("Wrong type of input!")
else:
    print(filtered1)








