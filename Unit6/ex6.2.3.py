def format_list(my_list):
    str = my_list[0] + ", " 
    str += ", ".join(my_list[2:-1:2])
    str += ", and " + my_list[-1]
    return str

def main():
    my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
    print(format_list(my_list))

if __name__ == "__main__":
    main()