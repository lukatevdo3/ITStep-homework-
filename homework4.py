#1

str1 = input("Enter Wanted String: ")
print(str1.encode()) #UTF-8 default-ია

#2

str2 = input("\nEnter Wanted String: ")
str2 = "'Python' " + str2.strip(' ').lower()

if "python" in str2:
    str2 = str2.replace("python", "Python")
    print(str2)
else:
    print(str2)

#3

text = input("\nEnter Wanted String: ")
a = text[0:int(len(text)/2)+1]
print(a)

#4

str3 = input("\nEnter Wanted String: ")
print(str3.isalnum())

#5

str4 = input("\nEnter Wanted String: ")
byte_version = str4.encode()
print(byte_version)
string_version = byte_version.decode()
print(string_version)