class Book:
    def __init__(self, title, author, price):
        # Store the received values inside the object
        self.title = title
        self.author = author
        self.price = price


# Read book details
title = input().strip()
author = input().strip()
price = int(input())

# Create Book object
book = Book(title, author, price)

# Display book details
print("BOOK DETAILS")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Price: {book.price}")