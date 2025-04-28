# good practices
# reference gpt :https://chatgpt.com/share/67fcb167-cac4-8008-95e5-4fe192bc9a8c
# reference sheet : https://docs.google.com/spreadsheets/d/11Y_yLw-s-b2LCuthccwawi6KYpDcmGOmY5V9Yr7w4Ms/edit?usp=sharing

a = True
value = 1 if a else 0
print(value)

# def user_info(user):
#   # return 'Name: {user.name} Age: {user.age}'.format(user=user) or
#   return  f"Name : {user.name} Age: {user.age}"
squares = [i * i for i in range(10) if i % 2 == 0]
# for i in range(1,11):
#     squares.append(i*i)
print(squares)
fruits = ['apple', 'banana', 'cherry']
for index, fruits in enumerate(fruits, start=0):
    print(index, fruits)
names = ["a", "b", "c", "d"]
numbers = [1, 2, 2, 3, 4]
age = [12, 13, 14]
for word, number, age in zip(names, numbers, age):
    print(word, number, age)
from collections import defaultdict

scores = defaultdict(int)
scores['venu'] += 10
scores['gopal'] += 5
print(scores)
# Without defaultdict, you'd get a KeyError unless you initialized 'venu' and 'gopal'.
from collections import Counter

c = Counter('banana')
print(c)  # Counter({'a': 3, 'n': 2, 'b': 1})

words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counter = Counter(words)

print(counter)  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})


# rows = int(input("Rows: "))
# cols = int(input("Cols: "))
#
# matrix = []
# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)
# result = []
# for i in range(len(matrix[0])):
#     new_row = []
#     for each_row in matrix:
#         new_row.append((each_row[i]))
#     result.append(new_row)
# print(result)


# -------------------> recursion ------------------------------->

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


result_factorial = factorial(5)
print(result_factorial)


def sum_of_numbers(n):
    if n == 0:
        return n
    return (n % 10) + sum_of_numbers(n // 10)


result_sum_of_numbers = sum_of_numbers(123)
print(result_sum_of_numbers)


def generate_subsets(s, index=0, current=""):
    if index == len(s):
        print(current)
        return
    generate_subsets(s, index + 1, current + s[index])  # include
    generate_subsets(s, index + 1, current)  # exclude


def no_of_ways(n):
    if n == 0 or n == 1:
        return 1
    return no_of_ways(n - 1) + no_of_ways(n - 2)


result_of_ways = no_of_ways(10)
print(result_of_ways)


# ------------------> ER Models--------------->
#  so every time we will consider biggest relation first
# for example let's take this scenario a doctor and appointments
# so a doctor can take multiple appointments(one to many)  and on other side one appointment belongs to one
# doctor(one to one) so in this case will take (one to many) and well keep primary key in many side in this case
# will keep doctor's table primary key in the appointment table as foreign key

class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.number = number
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance, interest):
        super().__init__(account_number, owner, balance)
        self.interest = interest


# -------------------------------------------- Dependency Inversion----------------------------------

# ok bro
# now i understood it one of the principle in clean architecture so
# in my cabin booking
# i wrote db storages in one file and
# interactors in another file
# so i am calling that business logic in interactor file
# and calling bd hits in storages files
# so when i am testing i am creating a fake data for interactor file and i am testing that.
# so i am not facing any struggle in db hits so this is the dependency inversion i guess.

# this is the dependency inversion


# -----------------------------> Design patterns --------------------->

# Adapter
# so lets a example if one class is producing a XML data and another class is accepting json
# so in this scenario we use adapter so change the type of data.
# let's take stock market example if it's extracting data in XML format then analytics
# example
class RoundHole:
    def fit(self, radius):
        print(f"Fitting round peg with radius {radius}")


class SquarePeg:
    def __init__(self, width):
        self.width = width


import math


class SquarePegAdapter:
    def __init__(self, square_peg):
        self.square_peg = square_peg

    def get_radius(self):
        return (self.square_peg.width * math.sqrt(2)) / 2


hole = RoundHole()
square_peg = SquarePeg(10)
adapter = SquarePegAdapter(square_peg)
hole.fit(adapter.get_radius())


# Decorator
# decorators are just wrappers that add extra behavior to a function without changing its actual code.
# examples
def uppercase_decorator(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


@uppercase_decorator
def say_hello():
    return "hello VenuGopal Adusumalli!"


print(say_hello())

# observer
# Observer pattern = Auto-notification system
#
# Whenever the Subject changes, it notifies all its Observers immediately —
# without the observers having to check manually.
# How it is useful in Django
# if in Django we will have a signals if a new user is create the we want to do add some courses then we emit
# some signals receivers will receive those signals and will perform some actions
# 🎯 What Is the Observer Pattern? (Real Life Example)
# Imagine this:
#
# You follow Virat Kohli on Instagram 🏏
# Whenever he posts something, you get a notification on your phone, right?
#
# So...
#
# Virat Kohli = The main source = Subject ✅
#
# You (Follower) = The observer/listener ✅
#
# Whenever he posts = All followers get notified = Automatic update 🔔

# Iterator
# Iterator pattern lets you access elements of a collection (like list, set, dictionary, etc.) one at a time without
# knowing the internal structure of that collection.
#
# Concept	Meaning
# iter(obj)	Converts any iterable to an iterator
# next(obj)	Gets the next element
# StopIteration	Raised when no more items are left

# so internally Django will have iterator itself
# so if we query objects.all() it automatically creates iterator


# Template Method
# “A base class defines the skeleton of an algorithm, and subclasses override specific steps without
# changing the overall structure.”


# ----------------------------------->DB indexes------------------>

# DB indexes
# These are used to increased  the speed of queries so in the database it will store the indexes so while querying it
# will act as book indexes if search value is less than root value it will go left vice versa

# An index is a data structure that improves the speed of data retrieval.
# Works like a table of contents in a book.
#
# 🌳 What Data Structure is Used?
# Most databases (like MySQL/PostgreSQL) use a B-Tree (Balanced Tree).
# B-Tree stores values in sorted order and allows fast search, insert, delete in O(log n) time.
# How B-Tree Works (Example):
# Given emails: ['anu', 'kiran', 'raj', 'sruthi', 'venu']
#
# Sorted order: ['anu', 'kiran', 'raj', 'sruthi', 'venu']
#             [     raj     ]
#           /                \
# [anu, kiran]           [sruthi, venu]
# Searching kiran? Start at raj → go left → found.
#
# Searching venu? Start at raj → go right → found.
# so when index is set it is stored a b tree i won't stored as number in rows or column.
# so how does multi index stores?


print("----------------------------Recursion---------------------")

x = int(input())
# GraphQL
# GraphQL is a query language for APIs and a runtime for executing those queries on your data.
#
# Instead of multiple REST API endpoints, GraphQL gives you a single endpoint where you can send precise queries to get exactly the data you need, nothing more, nothing less.
#
# Key Features:
# 📦 Get all related data in one request (no over-fetching or under-fetching)
#
# 🎯 Clients define what they want (you can specify which fields you want returned)
#
# 🚀 Strongly typed schema (backend defines what data can be queried)
#
# ⚡ Real-time support (via subscriptions)
