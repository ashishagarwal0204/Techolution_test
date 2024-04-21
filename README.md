# Library Management System

This is a simple Library Management System implemented in Python. It allows users to manage books, users, and checkouts.

## Features

- Add, update, delete, list, and search books by various attributes like title, author, or ISBN.
- Add, update, delete, list, and search users by attributes like name and user ID.
- Check out and check-in books.
- Track book availability.
- Simple logging of operations.

## File Structure

- `book.py`: Contains the Book class and BookManager for managing books.
- `user.py`: Contains the User class and UserManager for managing users.
- `check.py`: Contains the Checkout class and CheckoutManager for managing checkouts.
- `models.py`: Contains simple data models for Book, User, and Checkout.
- `storage.py`: Contains the JSONStorage class for reliable storage and retrieval using JSON files.
- `main.py`: Main script for user interaction and orchestration of functionalities.

## Usage

1. Run `main.py` to start the Library Management System.
2. Follow the prompts to perform various operations like adding books, adding users, checking out books, etc.
