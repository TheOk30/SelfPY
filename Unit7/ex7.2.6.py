def main():
    products = input("Enter a string of products separated by commas: ").split(",")

    while True:
        print("Menu:")
        print("1. Print the list of products")
        print("2. Print the number of products in the list")
        print("3. Check if a product is on the list")
        print("4. Count the number of occurrences of a product")
        print("5. Delete a product from the list")
        print("6. Add a product to the list")
        print("7. Print invalid products")
        print("8. Remove duplicates from the list")
        print("9. Exit")

        choice = int(input("Enter your choice 1-9: "))
        match choice:
            case 1:
                print(products)
            case 2:
                print(len(products))
            case 3:
                product = input("Enter a product name: ")
                if product in products:
                    print("The product is on the list.")
                else:
                    print("The product is not on the list.")
            case 4:
                product = input("Enter a product name: ")
                print(products.count(product))
            case 5:
                product = input("Enter a product name: ")
                products.remove(product)
            case 6:
                product = input("Enter a product name: ")
                products.append(product)
            case 7:
                invalid_products = [p for p in products if len(p) < 3 or not p.isalpha()]
                print(invalid_products)
            case 8:
                products = list(set(products))
            case 9:
                break

if __name__ == "__main__":
    main()