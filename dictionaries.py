#1.Create a dictionary with three key-value pairs representing a student's information: name, age, and grade. Print each key-value pair on a new line.
def dictionary():
    student_info = {'name': 'Deirdre', 'age':20 , 'grade':'A'}
    for key, value in student_info.items():
        print(f"{key} : {value}")
dictionary()

#2.Write a function that takes a dictionary of people's names and their ages, {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of people who are 21 or older.
def age():
    information ={'Alice': 24, 'Bob': 19, 'Charlie' : 30}
    older = []
    for age in information:
        if information[age] >= 21:
            older.append(age)
    print(f"People who are older than 21: {older}")
age()

#3.Given a dictionary representing items in a store with their prices, {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that takes a list of items bought, ['apple', 'orange', 'banana', 'banana'], and calculates the total cost.
def items():
    item_prices = {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}
    items_bought = ['apple', 'orange', 'banana', 'banana']
    total_cost = 0
    for item in items_bought:
        total_cost += item_prices[item]
    print(f"The total cost of the items is: {total_cost}")
items()

#4.Write a program that counts the occurrences of each word in a given sentence. Example: for the sentence "hello world hello," the output should be {'hello': 2, 'world': 1}.
def word_count():
    sentence = "hello world hello"
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    print(word_count)
word_count()
