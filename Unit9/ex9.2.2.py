def copy_file_content(source, destination):
    with open(source, "r") as source_file:
        with open(destination, "w") as destination_file:
            for line in source_file:
                destination_file.write(line)
def main():
    copy_file_content("copy.txt", "paste.txt")

if __name__ == "__main__":
    main()