def main():
    str = input("Please enter a string: "); # astronaut
    output = str[:len(str)//2].lower() + str[len(str)//2:].upper();
    print(output)
    # astrONAUT
if __name__ == "__main__":
    main()