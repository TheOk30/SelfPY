def distance(num1, num2, num3):
    condition1 = abs(num1 - num2) == 1 or abs(num1 - num3) == 1
    condition2 = abs(num2 - num3) >= 2 and abs(num2 - num1) >= 2 or abs(num3 - num1) >= 2
    return condition1 and condition2

print(distance(1, 2, 10)) # True

print(distance(4, 5, 3)) # False
