def main():
    inputnum = int(input("Enter three digits (each digit for one pig): ")) #124

    sum_digits = inputnum%10 + inputnum //100 + inputnum//10%10
    print("sum of digits:", sum_digits)  #7

    print("bricks evenly distributed:", sum_digits // 3) #2

    print("remeinder of bricks:", sum_digits % 3) #1

    print("is evenly distributed:", sum_digits % 3 == 0) #False

if __name__ == "__main__":
    main()