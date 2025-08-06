array_length = int(input())
array = list(map(int, input().split()))
number_of_rotations = int(input())
index = array_length - number_of_rotations
new_array = array[index:] + array[:index]
print(new_array)

