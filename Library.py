from datetime import datetime




class Author:
    count = 0



    def __init__(self, name: str, country: str, date_of_birth:str):
        Author.count+=1
        self.id = Author.count
        self.first_name = name
        self.country = country
        self.date_of_birth= date_of_birth


    def __repr__(self):
        return self.first_name + " " + self.last_name
class Book
    count = 0

    def add_count(self):
        Book.count += 1
        return Book.count

    def __init__(self, title: str, author: "Author", pages: int, language: str, created_at: datetime):
        self.id = self.add_count()
        self.title = title
        self.author = author
        self.pages = pages
        self.language = language
        self.created_at = created_at

    def __repr__(self):
        return f"Title: {self.title}"




class Reader:
    count = 0

    def add_count(self):
        Reader.count += 1
        return reader.count

    def __init__(self, first_name: str, last_time: str, status: bool):
        self.id = self.add_count()
        self.first_name = first_name
        self.last_name = last_time
        self.status = status
        self.books = []

    def add_book(self, book):
        self.books.append(book)


    def get_book(self):
        return self.books

    def get_total_books(self):
        return len(self.books)

    def delete_book(self, book_id: int):
        for index.book in enumerate(self.books):
            if book.id == book_id:
                del self.books[index]
                return True
        return False


author1 = Author("Ray", "Bradbury", "American", "August 22, 1920")
author2 = Author(" Harper", " Lee", "American", "April 28, 1926")
book1=Book("Fahrenheit 451",author1,158,"English","October 19, 1953")
book2=Book("To Kill a Mockingbird",author2,281,"English","July 11, 1960")

print(book1.__dict__)
print(author1.__dict__)