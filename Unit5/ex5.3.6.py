def fix_age(age):
    if age >= 13 and age <= 19 and age not in (15, 16):
        return 0
    return age


def filter_teens(a=13, b=13, c=13):
    return fix_age(a) + fix_age(b) + fix_age(c)

print(filter_teens())  # 0
print(filter_teens(1, 2, 3))  # 6
print(filter_teens(2, 1, 15))  # 18