def last_early(my_str):
    return my_str[-1].lower() in my_str[:-1].lower()

print(last_early("happy birthday"))  # True
print(last_early("best of luck"))  # False
print(last_early("Wow"))  # True
print(last_early("X"))  # False

