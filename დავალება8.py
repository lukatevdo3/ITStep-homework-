#1

def func_1(N):

    a , b = 0, 1 
    arr = [a, b]   
    
    while True:
       
        a , b = b, a+b
       
        arr.append(b)

        if arr.index(b) == N:
           break

    return arr


print(func_1(int(input("Enter a Number: "))))    

#2

def func_2(string1, string2):

    string1 = string1.lower()
    string2 = string2.lower()

    set1 = set()
    set2 = set()

    if len(string1) == len(string2):
        for i in string1:
            set1.add(i)

        for k in string2:
            set2.add(k)

        if set1 == set2:
            return True
        else:
            return False
    else:
        print("It is not True!!")
      
   

print(func_2(input("Enter First String: "), input("Enter Second String: ")))    

#3

def func_3(N):

    k1 = 1

    for i1 in range(1, N+1):
        k1 *= i1
        i1 += 1
        

    return k1

print(func_3(int(input("Enter a Number: "))))

#4

def func_3(text, symbol):
    count = 0
    for char in text:
        if char == symbol:
            count += 1
    return count

print(func_3(input("Enter a String: "), input("Enter a Symbol: ")))





           
