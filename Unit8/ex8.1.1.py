def main():
    tuple_one = (1, 2, 3, 4)
    print(tuple_one[1:-1]) # (2, 3)

    tuple_two = (2, 5, 8, 3, 6, 9)
    for i in range(0, len(tuple_two), 3 ):
        print(tuple_two[i]) 
    
    # 2
    # 3

    tuple_three = (2, 1, 3)
    tuple_three.sort() # error message

    tuple_four = (4, 2, 3)
    sorted(tuple_four) # [4, 2, 3]     




if __name__ == "__main__":
    main()