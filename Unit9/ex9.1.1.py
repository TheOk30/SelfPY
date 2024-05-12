def are_files_equal(file1, file2):
    with open(file1, "r") as f1:
        f1_content = f1.read()
    with open(file2, "r") as f2:
        f2_content = f2.read()
    return f1_content == f2_content

def main():
    are_files_equal("c:\vacation.txt", "c:\work.txt")
    # False

if __name__ == "__main__":
    main()