#~ library.py

books = []
issued_books = {}

#^ add books with price
def add_book():
    name = input("Enter book name: ")
    price = float(input("Enter rent price (₹): "))
    books.append({"name": name, "price": price})
    print("Book added successfully!\n")

#^ show books
def show_book():
    if len(books) == 0:
        print("No books available\n")
    else:
        print("\nAvailable Books:")
        for b in books:
            print(f"{b['name']} - Rent: ₹{b['price']}")
        print()

#^ payment method
def make_payment(amount):
    print(f"\nTotal amount to pay: ₹{amount}")
    print("Choose payment method:")
    print("1. UPI")
    print("2. Card")
    print("3. Cash")

    choice = int(input("Enter payment option: "))

    if choice in [1, 2, 3]:
        print("Payment successful!\n")
        return True
    else:
        print("Invalid payment method. Payment failed.\n")
        return False

#^ issue books
def issue_book():
    show_book()
    name = input("Enter book name to issue: ")

    for b in books:
        if b["name"] == name:
            if make_payment(b["price"]):
                books.remove(b)
                user = input("Enter your name: ")
                issued_books[name] = user
                print(f"Book issued to {user}\n")
            return

    print("Book not available\n")

#^ return books
def return_book():
    name = input("Enter book name to return: ")

    if name in issued_books:
        user = issued_books[name]
        del issued_books[name]
        books.append({"name": name, "price": 100})  
        print(f"Book returned by {user}\n")
    else:
        print("No such issued book found\n")

#^ main menu
def library():
    while True:
        print("====== Library Menu ======")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        try:
            choice = int(input("Enter choice: "))
        except:
            print("Invalid input\n")
            continue

        if choice == 1:
            add_book()
        elif choice == 2:
            show_book()
        elif choice == 3:
            issue_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print("Thank you!")
            break
        else:
            print("Invalid choice\n")

#? run
library()