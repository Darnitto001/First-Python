temperature = 45
if temperature > 25 :
    print("Temperature is too high")
else :
    print("Temperature is too low")


#A program that returns the smallest number
first = 50
second = 60
third = 70
if first < second and first < third :
    print(first, "Is the smallest Number")
elif second < first and second < third :
    print(second, "Is the smallest Number")
else :
    print(third, "Is the smallest Number")


#Checking if a number is an even number
number = 0
if number == 0 :
    print(number, "is a neutral number")
elif number % 2 == 0:
    print(number, "is even")
else :
    print(number, "is odd")