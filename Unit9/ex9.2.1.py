def main():
    with open("empty.txt", "w") as input_file:
        input_file.write("So, call me maybe?")
        print(input_file.read())
    
    # error

if __name__ == "__main__":
    main()