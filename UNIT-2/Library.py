# Develop a Library class that has instance variables like book_name, author, and availability status. The class should provide methods to check out a book, return a book, and display available books. Use the __init__ constructoe to initialize book details for each object.
class Library:
    def __init__(self, book_name, author, availability_status):
        self.book_name = book_name
        self.author = author
        self.availability_status = availability_status

    def check_out_book(self):
        if self.availability_status == "available":
            self.availability_status = "checked out"
            print("Book checked out successfully.")
        else:
            print("Book is already checked out.")

    def return_book(self):
        if self.availability_status == "checked out":
            self.availability_status = "available"
            print("Book returned successfully.")
        else:
            print("Book was not checked out.")

    def display_available_books(self):
        if self.availability_status == "available":
            print(f"Book: {self.book_name}, Author: {self.author}")

Reader1 = Library("The Great Gatsby", "F. Scott Fitzgerald", "available")
Reader2 = Library("1984", "George Orwell", "available")


print(Reader1.check_out_book())
print(Reader2.return_book())
print(Reader2.display_available_books())