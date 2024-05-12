def main():
    i = 11
    while i > 0:
        i -= 1    
        if i == 5:   
            break        
        print(i)

    # 10
    # 9
    # 8
    # 7
    # 6

    i = 11
    while i > 0:
        i -= 1    
        if i == 5:   
            continue         
        print(i)
    
    # 10
    # 9
    # 8
    # 7
    # 6
    # 4
    # 3
    # 2
    # 1
    # 0

if __name__ == "__main__":
    main()