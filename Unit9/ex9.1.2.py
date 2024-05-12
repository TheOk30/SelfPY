def main():
    file_path = input("Enter a file path: ")
    task = input("Enter a task: ")
    with open(file_path, 'r') as f:
        lines = f.readlines()
    if task == 'sort':
        words = sorted(set(line.split() for line in lines))
        print(words)
    elif task == 'rev':
        reversed_lines = [line[::-1] for line in lines]
        print(reversed_lines)
    elif task == 'last':
        n = int(input("Enter a number: "))
        print(lines[-n:])

if __name__ == "__main__":
    main()