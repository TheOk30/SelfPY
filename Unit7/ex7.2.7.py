def arrow(my_char, max_length): 
    for i in range(1, max_length+1):
        print((my_char + ' ') * i )
    for i in range(max_length-1, 0, -1):
        print((my_char + ' ') * i )

def main():
    print(arrow('*', 5))
    """
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * *
    * * *
    * *
    *
    """
if __name__ == "__main__":
    main()