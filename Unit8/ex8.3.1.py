def main():
    # 1:
    my_dict = {(1, 2): 1, (2, 3): 2}

    for key in my_dict.keys():
        print(key)
    
    #(1,2) and (2,3)

    # 2:
    for value in my_dict.values():
        print(value)
    
    #1 and 2

    # 3:
    print(len(my_dict))
    
    #2

    # 4:
    print(my_dict[1])
    
    #KeyError

    # 5:
    print(my_dict[1, 2])
    
    #1



if __name__ == "__main__":
    main()