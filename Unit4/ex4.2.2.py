def main():
    
    str = input("Enter a word: ") # Borrow or rob --> This is a palindrome

    if str == reversed(str):
        print("This is a palindrome")
    else:
        print("This is not a palindrome")

if __name__ == "__main__":
    main()