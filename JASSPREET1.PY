Shopping_cart = {}

def AddProduct():
    if len(Shopping_cart) >= 5:
        print("Cart is full.")
    else:
        ProductName = input("Enter the name of the product - ")
        BrandName = input("Enter the brand of the product - ")
        Shopping_cart[ProductName] = BrandName
        print("Product added to cart.")

def SearchProduct():
    productName = input("Enter the name of the product to search - ")
    if productName in Shopping_cart:
        print(f"{productName} found in cart. Brand: {Shopping_cart[productName]}.")
    else:
        print("No product exists with this name.")

def DeleteProduct():
    if len(Shopping_cart) == 0:
        print("Cart is empty, no item is found.")
    else:
        ProductName = input("Enter the name of the product to delete - ")
        if ProductName in Shopping_cart:
            del Shopping_cart[ProductName]
            print(f"{ProductName} removed from cart.")
        else:
            print("No product exists with this name.")

while True:
    print("WELCOME TO THE AMANDO SHOPPING SITE")
    print("A. Add product to the cart.")
    print("B. Search the product.")
    print("C. Delete the product from the cart.")
    print("D. Quit.")
    choice = input("Enter your choice (A/B/C/D): ")

    if choice.lower() == 'a':
        AddProduct()
    elif choice.lower() == 'b':
        SearchProduct()
    elif choice.lower() == 'c':
        DeleteProduct()
    elif choice.lower() == 'd':
        print("Thank you for using Amando Shopping Site!")
        break
    else:
        print("Invalid choice. Please enter a valid choice (A/B/C/D).")