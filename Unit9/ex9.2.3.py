def who_is_missing(file_name):
    # 8,1,9,7,4,6,3,2
    num = []
    with open(file_name, "r") as f:
        for line in file_name:
            num.append(int(line))
    num.sort()
    for i in range(1,len(num)):
        if num[i] != i:
            return num
    return -1

def main():
    who_is_missing("c:\findMe.txt")
    

if __name__ == "__main__":
    main()