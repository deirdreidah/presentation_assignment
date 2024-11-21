#1.Create a list of 5 fruits and print each fruit on a new line using a for loop.
def fruit():
    fruits = ['apples','pineapples','bananas','mangoes','oranges']
    for fruit in fruits:
        print(fruit)
        print("\n")
fruit()

#2. Write a function that takes a list of numbers and returns a new list with each number squared. Example: [1, 2, 3] should become [1, 4, 9].
def square_numbers():
    list = [1,2,3]
    squared_list = []
    for num in list:
        squared_list.append(num ** 2)
    return(squared_list)
square_numbers()

#3.Write a Python program that takes two lists, list1 = [1, 2, 3] and list2 = [4, 5, 6], and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].
def single_list():
    list1 = [1,2,3]
    list2 = [4,5,6]
    combined = []
    for a,b in zip(list1,list2):
        combined.append(a)
        combined.append(b)
    print(combined)
single_list()

#4.Given a list of numbers, [3, 1, 4, 1, 5, 9, 2], write a program to the two largest numbers in the list without using the max() function.
def largest():
    numbers = [3, 1, 4, 1, 5, 9, 2]
    numbers.sort(reverse= True)
    largest = numbers[0]
    second_largest = numbers[1]
    print(numbers)
    print(f"The largest number is {largest}.")
    print(f"The second largest number is {second_largest}.")
largest()
