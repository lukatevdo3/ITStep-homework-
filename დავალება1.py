#დავალება პირველი
#1
num1 = 14
num2 = 5

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 ** num2)

#2
d1 = eval(input("შეიყვანეთ პირველი დიაგონალის სიგრძე: "))
d2 = eval(input("შეიყვანეთ მეორე დიაგონალის სიგრძე: "))

print(d1*d2/2)

#3
meter_to_cm = 100
meter_to_mm = 1000
meter_to_mile = 0.0006
meter_to_decimeter = 10
meter = eval(input("შეიყვანეთ სასურველი მეტრი: "))

print(meter_to_cm * meter, "სანტიმეტრი")
print(meter_to_decimeter * meter, "დეციმეტრი")
print(meter_to_mile * meter, "მილი")
print(meter_to_mm * meter, "მილიმეტრი")

#4
base = eval(input("შეიყვანეთ სასურველი ფუძის სიგრძე: "))
h = eval(input("შეიყვანეთ სასურველი სიმაღლის სიგრძე: "))

print("სამკუთხედის ფართობია", base*h/2)

#5
n = eval(input("შეიყვანეთ ნებისმიერი ორნიშნა რიცხვი: "))

if n >=10 and n <100:
   print((n%10) + (n//10))
else:
   print("შეყვანილი რიცხვი არასწორია, გთხოვთ შეიყვანეთ ორნიშნა რიცხვი")


