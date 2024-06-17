from abc import ABC, abstractmethod

# Abstract base class representing a generic item
class Item(ABC):
    def __init__(self, name, item_type):
        self.name = name
        self.item_type = item_type

    @abstractmethod
    def display_info(self):
        pass

# Book class inheriting from Item
class Book(Item):
    def __init__(self, name, author, genre):
        super().__init__(name, "Book")
        self.author = author
        self.genre = genre

    def display_info(self):
        print(f"Book: {self.name}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")

# DVD class inheriting from Item
class DVD(Item):
    def __init__(self, name, director, duration):
        super().__init__(name, "DVD")
        self.director = director
        self.duration = duration

    def display_info(self):
        print(f"DVD: {self.name}")
        print(f"Director: {self.director}")
        print(f"Duration: {self.duration} minutes")

# Journal class inheriting from Item
class Journal(Item):
    def __init__(self, name, issue_number, publish_date):
        super().__init__(name, "Journal")
        self.issue_number = issue_number
        self.publish_date = publish_date

    def display_info(self):
        print(f"Journal: {self.name}")
        print(f"Issue Number: {self.issue_number}")
        print(f"Publish Date: {self.publish_date}")

# Member class for managing member interactions
class Member:
    def request_item(self):
        return input("Enter the name of the item you want to borrow: ")

    def return_item(self):
        return input("Enter the name of the item you are returning: ")

# Library class managing the collection of items
class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.items = []

    def display_available_items(self):
        print(f"Items available in {self.library_name}:")
        if self.items:
            for item in self.items:
                item.display_info()
                print()  # for spacing between items
        else:
            print("No items available.")

    def lend_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                print(f"You have borrowed '{item_name}'. Please return it within 30 days.")
                self.items.remove(item)
                return
        print(f"Sorry, '{item_name}' is not available in {self.library_name}.")

    def add_item(self, item):
        self.items.append(item)
        print(f"'{item.name}' has been added to {self.library_name}.")

    def return_item(self, item_name):
        # In a real scenario, we would have a database or a more sophisticated way of managing borrowed items
        print(f"Thank you for returning '{item_name}'. If it belongs to {self.library_name}, it will be processed accordingly.")

# Example usage
if __name__ == "__main__":
    library = Library("Central Library")
    member = Member()

    # Adding some initial items to the library
    book1 = Book("Python Programming", "John Smith", "Programming")
    book2 = Book("Java Basics", "Emily Brown", "Programming")
    book3 = Book("Machine Learning", "David Johnson", "Artificial Intelligence")
    dvd1 = DVD("Inception", "Christopher Nolan", 148)
    journal1 = Journal("Nature", 123, "2020-05-01")

    library.add_item(book1)
    library.add_item(book2)
    library.add_item(book3)
    library.add_item(dvd1)
    library.add_item(journal1)

    while True:
        print("\nMenu:")
        print("1. Display available items")
        print("2. Request an item")
        print("3. Return an item")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == '1':
            library.display_available_items()
        elif choice == '2':
            requested_item = member.request_item()
            library.lend_item(requested_item)
        elif choice == '3':
            returned_item = member.return_item()
            library.return_item(returned_item)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
