def numbers_letters_count(my_str):
    new_list = [0, 0]

    for i in my_str:
        if i.isdigit():
            new_list[0] += 1
        else:
            new_list[1] += 1
    return new_list

def main():
    print(numbers_letters_count("Python 3.6.3")) # []

if __name__ == "__main__":
    main()