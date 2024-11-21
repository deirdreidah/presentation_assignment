#1.Create a class called Car with attributes brand and color. Instantiate an object of the Car class and print its attributes.
#2.Add a method called start_engine to the Car class that prints a message saying the engine of the car has started. Create an instance of Car and call the method.
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
         print(f"The engine of the {self.color} {self.brand} has started.")

my_car = Car("Mercedes", "Silver")
print(f"Brand: {my_car.brand}")
print(f"Color: {my_car.color}")

my_car.start_engine()

## Advanced: 
# Create a class called BankAccount with attributes account_number and balance. Add methods to:
# Deposit an amount.
# Withdraw an amount (only if sufficient balance exists).
# Print the account balance.

class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited {amount} to account {self.account_number}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print(f"Insufficient balance to withdraw {amount} from account {self.account_number}.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")

    def print_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")


account = BankAccount("12345698", initial_balance=500)
account.deposit(200)
account.print_balance()
account.withdraw(100)
account.print_balance()
account.withdraw(700)
account.print_balance()
account.deposit(-50)
account.withdraw(-100)




# Challenge: 
# Implement a class called Library that manages a collection of books. Each book has a title, author, and available status. 
# The Library class should have methods to:
# Add a book to the library.
# Remove a book from the library.
# Check if a book is available by title.
# Borrow a book (mark it as unavailable if it’s available).
# Return a book (mark it as available again if it was borrowed).


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def _str_(self):
        return f"'{self.title}' by {self.author} ({'Available' if self.is_available else 'Unavailable'})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added to the library.")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")

    def check_availability(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.is_available
        print(f"Book '{title}' not found in the library.")
        return False

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.is_available = False
                    print(f"You have borrowed '{title}'.")
                else:
                    print(f"Book '{title}' is currently unavailable.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_available:
                    book.is_available = True
                    print(f"Book '{title}' has been returned.")
                else:
                    print(f"Book '{title}' was not borrowed.")
                return
        print(f"Book '{title}' not found in the library.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)


library = Library()
library.add_book("King of Wrath", "Ana Huang")
library.add_book("2022", "Coleen Hoover")
print("\n")

library.check_availability("2022")
library.borrow_book("2022")
library.check_availability("2022")
library.return_book("2022")
library.remove_book("King of Wrath")


