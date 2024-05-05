def main():

    #1
    true_or_false = "ron" != "ron" #False

    #2
    true_or_false = "a" in "alpha" #True

    #3
    true_or_false = "A" in "alpha" #False

    #4
    true_or_false = "alpha" < "beta" #True

    #5
    true_or_false = 1 < 2 < 1 #False

    #6
    true_or_false = 18 <= 22 < 30 #True

    #7
    true_or_false = not(10) #False

    #8
    true_or_false = (7 > 10) and (1 > 1) #False

    #9
    true_or_false = (20 % 10 == 2) or (1 == 1) #True
    
if __name__ == "__main__":
    main()