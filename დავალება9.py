# #1

# def func_1(N):

#     int_list.append(N)

#     return int_list

# # ======================

# int_list = [10,20,30,40]
# appended = func_1(int(input("Enter any number: ")))

# print(appended)

# #2

# def func_2(*args):

#     sum = 0
    
#     for i in args:
#         sum = sum + i 
    
#     print(sum)

# # =======================    
    
# arr = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
# func_2(*arr1)  

# #3

# def func_3(str1):

#     gl_str = "Local"
#     print(gl_str)

# # ========================

# gl_str = "Global"
# func_3(input("Enter literally anything: "))

# #4

# def sum_digits(number):
#     if number == 0:
#         return 0
#     return number % 10 + sum_digits(number // 10)

# # ========================

# print(sum_digits(int(input("Enter a Number: "))))   

# #5

def reverse(string1):
    if string1 == None:
        return

    for i in string1:
        arr.append(i)
        return reverse(string1.replace(i, '', 1))

    
    arr.reverse()
    word = ''.join(arr)
    print(word)

# # ========================

arr = []
string2 = input("Enter Your String: ")
reverse(string2)














    