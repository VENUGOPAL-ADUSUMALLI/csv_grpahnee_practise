# example 1
square = [i * i for i in range(10)]
print(square)

# example 2
my_list = [1, 2, 3, 4, 5]
if my_list:
    print("List is not empty")

# example 3
a = 5
b = 3
a, b = b, a
print(a, b)

# example 4
my_dict = {"a": 10, "b": 20}
get_a = my_dict.get("a")
for key, value in my_dict.items():
    print(key, value)
print(get_a)

# example 5
fruits = ["apple", "banana", "cherry"]
for index, fruits in enumerate(fruits):
    print(index, fruits)
nums = [1, 2, 3, 4, 5, 6]
even_nums = [n for n in nums if n % 2 == 0]
print(even_nums)
names = ["a", "b", "c", "d"]
numbers = [1, 2, 2, 3, 4]
age = [12, 13, 14]
for words, number, ages in zip(names, numbers, age):
    print(words, number, ages)


def transpose(matrix):
    return list(map(list, zip(*matrix)))


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transposed = transpose(matrix)
print(transposed)

# -----------------------------> Redis---------------------------->
