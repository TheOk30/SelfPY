def main():
    
    temp = input("Insert the temperature sensor you would like to convert: ").lower()
    
    if temp[-1] == 'f':
        temp = float(temp[:-1])
        print("The temperature in Celsius is: " + str((temp - 32) * 5/9)  + 'C')
    elif temp[-1] == 'c':
        temp = float(temp[:-1])
        print("The temperature in Fahrenheit is: "+  str((temp * 9/5)) + 32 + 'F')
    else:
        print("Please enter a valid temperature.")
        

if __name__ == "__main__":
    main()