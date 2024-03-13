from datetime import datetime

class Book:
    def __init__(self, title, author, price, quantity, category):
        # Initialize book attributes
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity
        self.category = category

    def display_details(self):
        # Display book details
        print(f"Title: {self.title}\nAuthor: {self.author}\nPrice: ${self.price}\nQuantity: {self.quantity}\nCategory: {self.category}")


class ShoppingCart:
    def __init__(self):
        # Initialize shopping cart
        self.items = []
        self.purchased_orders = []

    @staticmethod
    def check_stock(func):
        # Decorator function to check if there is sufficient stock
        def wrapper(self, book, quantity):
            if book.quantity >= quantity:
                return func(self, book, quantity)
            else:
                raise ValueError(f"Insufficient stock. Only {book.quantity} {book.title}(s) available.")
        return wrapper

    @check_stock
    def add_to_cart(self, book, quantity):
        # Add a book to the shopping cart
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.items.append((book, quantity))
        print(f"{quantity} {book.title}(s) added to cart.")

    def view_cart(self):
        # View items in the shopping cart
        if not self.items:
            print("Shopping Cart is empty.")
        else:
            total_price = 0
            print("Shopping Cart:")
            for index, (book, quantity) in enumerate(self.items, start=1):
                print(f"{index}. {book.title} - Quantity: {quantity}, Price: ${book.price}")
                total_price += book.price * quantity
            print(f"Total Price: ${total_price}")

    def purchase(self):
        # Purchase items in the shopping cart
        if not self.items:
            print("Shopping Cart is empty. No items purchased.")
        else:
            print("Items Purchased:")
            purchased_items = []
            for book, quantity in self.items:
                print(f"{book.title} - Quantity: {quantity}")
                purchased_items.append((book, quantity))
            purchase_date = datetime.now()  # Get current date and time
            order = Order(purchased_items, purchase_date)  # Pass purchase date to Order constructor
            self.purchased_orders.append(order)
            print("Purchase successful.")
            self.items = []

    def view_purchased_orders(self):
        # View purchased orders
        if not self.purchased_orders:
            print("No orders have been made yet.")
        else:
            print("Purchased Orders:")
            for index, order in enumerate(self.purchased_orders, start=1):
                order.display_order_details()
                print()

    def delete_book_from_cart(self, title):
        # Delete a book from the shopping cart
        if not self.items:
            print("Shopping Cart is empty.")
            return
        found = False
        for index, (book, _) in enumerate(self.items):
            if book.title.lower() == title.lower():
                del self.items[index]
                found = True
                print(f"Book '{title}' removed from cart.")
                break
        if not found:
            print(f"Book '{title}' not found in the shopping cart.")
    
    def search_order_by_id(self, order_id):
        # Search for an order by ID
        found_order = None
        for order in self.purchased_orders:
            if order.order_id == order_id:
                found_order = order
                break
        if found_order:
            print("Order found:")
            found_order.display_order_details()
        else:
            print("Order not found.")

class Order:
    order_id_generator = 1

    def __init__(self, items, purchase_date):
        # Initialize order attributes
        self.items = items
        self.order_id = Order.generate_order_id()
        self.purchase_date = purchase_date

    @staticmethod
    def generate_order_id():
        # Generate unique order ID
        order_id = Order.order_id_generator
        Order.order_id_generator += 1
        return order_id

    def display_order_details(self):
        # Display order details
        print(f"Order ID: {self.order_id}")
        print("Items Purchased:")
        for book, quantity in self.items:
            print(f"{book.title} - Quantity: {quantity}")
        print(f"Order Total: ${sum(book.price * quantity for book, quantity in self.items)}")
        print(f"Purchase Date: {self.purchase_date}")


class InventoryManagement:
    def __init__(self):
        # Initialize inventory
        self.inventory = []

    def add_book(self, book):
        # Add a book to inventory
        self.inventory.append(book)

    def view_inventory(self):
        # View inventory
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for index, book in enumerate(self.inventory, start=1):
                book.display_details()

    def search_inventory(self, title):
        # Search inventory by book title
        if not self.inventory:
            print("Inventory is empty.")
            return
        found_books = []
        for book in self.inventory:
            if title.lower() in book.title.lower():
                found_books.append(book)
        if not found_books:
            print("No matching books found.")
        else:
            print("Matching Books in Inventory:")
            for found_book in found_books:
                found_book.display_details()

    def get_books_by_category(self, category_name):
        # Get books by category
        category_books = [book for book in self.inventory if book.category.lower() == category_name.lower()]
        if not category_books:
            print("No books found in this category.")
        else:
            print(f"Books in Category '{category_name}':")
            for book in category_books:
                book.display_details()

    def search_by_category(self, category_name):
        # Search books by category
        found_books = [book for book in self.inventory if book.category.lower() == category_name.lower()]
        if not found_books:
            print(f"No books found in the category '{category_name}'.")
        else:
            print(f"Books in the category '{category_name}':")
            for book in found_books:
                book.display_details()


def main_menu():
    # Main menu of the system
    print("\n=== Welcome to the Student Bookstore Management System ===\n")
    print("1. View Inventory")
    print("2. Add a Book to Inventory")
    print("3. View Shopping Cart")
    print("4. Add Book to Shopping Cart")
    print("5. Purchase Books")
    print("6. View Purchased Orders")
    print("7. Delete Book from Shopping Cart")
    print("8. Search Inventory")
    print("9. View Books by Category")
    print("10. Search by Category")
    print("11. Search Order by ID")
    print("12. Exit")
    return input("\nEnter your choice: ")


if __name__ == "__main__":
    # Create some initial books
    book1 = Book("Python Programming", "Guido van Rossum", 29.99, 10, "Programming")
    book2 = Book("Data Structures and Algorithms", "John Doe", 39.99, 5, "Programming")
    book3 = Book("To Kill a Mockingbird", "Harper Lee", 15.00, 20, "Fiction")
    book4 = Book("1984", "George Orwell", 12.99, 15, "Fiction")

    # Create an inventory
    inventory = InventoryManagement()
    inventory.add_book(book1)
    inventory.add_book(book2)
    inventory.add_book(book3)
    inventory.add_book(book4)

    # Create a shopping cart
    cart = ShoppingCart()

    while True:
        try:
            choice = main_menu()

            if choice == '1':
                inventory.view_inventory()
            elif choice == '2':
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                price = float(input("Enter the price of the book: "))
                while True:
                    try:
                        quantity = int(input("Enter the quantity of the book: "))
                        if quantity < 0:
                            raise ValueError("Quantity must be a non-negative integer.")
                        break
                    except ValueError as e:
                        print(f"Error: {e}")
                category = input("Enter the category of the book: ")
                new_book = Book(title, author, price, quantity, category)
                inventory.add_book(new_book)
                print("Book added to inventory.")
            elif choice == '3':
                cart.view_cart()
            elif choice == '4':
                title = input("Enter the title of the book you want to add to the cart: ")
                found = False
                for book in inventory.inventory:
                    if book.title == title:
                        found = True
                        while True:
                            try:
                                quantity = int(input("Enter the quantity: "))
                                if quantity < 0:
                                    raise ValueError("Quantity must be a non-negative integer.")
                                break
                            except ValueError as e:
                                print(f"Error: {e}")
                        cart.add_to_cart(book, quantity)
                        break
                if not found:
                    print("Book not found in inventory.")
            elif choice == '5':
                cart.purchase()
            elif choice == '6':
                 cart.view_purchased_orders()
            elif choice == '7':
                title = input("Enter the title of the book you want to delete from the cart: ")
                cart.delete_book_from_cart(title)
            elif choice == '8':
                title = input("Enter the title of the book you want to search for: ")
                inventory.search_inventory(title)
            elif choice == '9':
                category_name = input("Enter the category name: ")
                inventory.get_books_by_category(category_name)
            elif choice == '10':
                category_name = input("Enter the category name: ")
                inventory.search_by_category(category_name)
            elif choice == '11':
                order_id = int(input("Enter the order ID: "))
                cart.search_order_by_id(order_id)
            elif choice == '12':
                print("Thank you for using the Student Bookstore Management System!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 12.")
        except Exception as e:
            print(f"An error occurred: {e}")
