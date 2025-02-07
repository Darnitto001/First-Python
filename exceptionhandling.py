try :
    number = 3
    print(number)
except :
    print("An error occured")
finally:
    print("Bye")


try:
    x = 67
    y = 0
    print(x / y)
except :
    print("ZeroDivisionError occured")