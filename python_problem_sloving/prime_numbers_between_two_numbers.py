first_number = int(input())
second_number = int(input())
string = ""
for i in range(first_number, second_number):
    if i == 1:
        continue
    elif i == 2 or i == 3 or i == 5 or i == 7:
        string += str(i) + " "
    elif i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        continue
    else:
        string += str(i) + " "
print(string)
