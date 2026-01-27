from actions import *
value_1 = int(input("Enter the first number: "))
value_2 = int(input("Enter the second number: "))
operators = input("Enter your desired operator:")

if operators == "+":
    res = add(value_1, value_2)
    print(res)
elif operators == "-":
    res= sub(value_1, value_2)
    print(res)
elif operators == "*":
    res= mul(value_1, value_2)
    print(res)
else:
    res =div(value_1, value_2)
    print(res)