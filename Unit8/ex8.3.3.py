def count_chars(my_str):
    new_dict = {}
    for i in my_str:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    return new_dict


def main():
    magic_str = "abra cadabra"
    count_chars(magic_str)

    #{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

if __name__ == "__main__":
    main()