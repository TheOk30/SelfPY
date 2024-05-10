def chocolate_maker(small, big, x):
    if x < 1:
        return False
    elif x == small or x == 5*big:
        return True
    else:
        return (small > 0 and chocolate_maker(small -1, big, x - 1) 
                or  big > 0 and chocolate_maker(small, big -1, x - 5))
    
print(chocolate_maker(3, 1, 8))
print(chocolate_maker(3, 1, 9))
print(chocolate_maker(3, 2, 10))