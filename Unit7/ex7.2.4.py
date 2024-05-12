def seven_boom(end_number):
    for i in range(1, end_number+1):
        if i % 7 == 0 or '7' in str(i):
            print("BOOM")
        else:
            print(i)

def main():
    print(seven_boom(17))

if __name__ == "__main__":
    main()