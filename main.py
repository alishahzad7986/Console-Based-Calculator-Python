from actions import *

operators = input("Enter your desired operator:")

if operators == "+":
    value_1 = int(input("Enter the  number: "))
    value_2 = int(input("Enter the  number: "))
    res = add(value_1, value_2)
    print(res)
elif operators == "-":
    value_1 = int(input("Enter the  number: "))
    value_2 = int(input("Enter second number: "))
    res= sub(value_1, value_2)
    print(res)
elif operators == "*":
    value_1 = int(input("Enter the  number: "))
    value_2 = int(input("Enter the  number: "))
    res= mul(value_1, value_2)
    print(res)
elif operators == "/":
    value_1 = int(input("Enter the  number: "))
    value_2 = int(input("Enter the number: "))
    res =div(value_1, value_2)
    print(res)
elif  operators == "2":
    value_1 = int(input("Enter your number: "))
    res= squ(value_1)
    print(res)
elif operators == "3":
    value_1 = int(input("Enter your number: "))
    res = cub(value_1)
    print(res)