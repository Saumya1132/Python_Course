# create class to represent a book with attributes like title , author and publication year

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        
# create an instance of the Book class

book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

# print the attributes of the book

print(f"Title: {book1.title}")

print(f"Author: {book1.author}")

print(f"Publication Year: {book1.publication_year}")