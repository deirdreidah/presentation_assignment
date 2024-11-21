 #LOOPS
#1.Write a Python program that prints all even numbers between 1 and 20 using a for loop.
def even_numbers():
    for number in range(2,21,2):
        print(number)
even_numbers()

#2.Use a while loop to ask the user to input a number until they provide a number greater than 10.
def greater_than():
    num = int(input("Enter the number: "))
    while num < 11:
        num = int(input("Enter a number greater than 10: "))
    else:
        print(f"{num} is greater than 10.")
greater_than()

#3.Write a program that prints the multiplication table (from 1 to 10) for numbers from 1 to 5 using nested for loops.
def multiple():
    for int in range(1,6):
        print(f"Multiplication table for {int}: ")
    for i in range(1,11):
        print(f"{int} x {i} = {int * i}")
    print("\n")
multiple()

#4. Given a list of integers, [4, 7, 2, 9, 12, 15], write a program using a for loop to find the sum of all odd numbers and print the result.
def odd_numbers():
    integers = [2,4,7,9,12,15]
    sum = 0
    for int in integers:
        if int % 2 != 0:
            sum += int
    print(f"The sum of all odd numbers in the list of integers is: {sum}")
odd_numbers()

