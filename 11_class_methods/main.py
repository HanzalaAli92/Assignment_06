# 11_class_methods
"""
Assignment:
Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added."""

class Book:
    total_books = 0  # Class variable jo total books ki ginti rakhta hai

    @classmethod
    def increment_book_count(cls):  # Class method jo book count ko barhata hai
        cls.total_books += 1  # Class variable total_books mein 1 add karte hain

if __name__ == "__main__":
    Book.increment_book_count()  # Book count 1 ho gaya
    Book.increment_book_count()  # Book count 2 ho gaya
    Book.increment_book_count()  # Book count 3 ho gaya
    
    print(f"Total books: {Book.total_books}")  # Total books print kar rahe hain