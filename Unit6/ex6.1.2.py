def shift_left(my_list):
    return my_list[1:] + [my_list[0]]

def main():
    print(shift_left(['monkey', 2.0, 1])) # [2.0, 1, 'monkey']

if __name__ == "__main__":
    main()

