word = input().split()
string = ""
palindrome = ""
for each_word in word:
    string += each_word.lower()
length = len(word)
for i in range(length):
    each = word[length - i - 1]
    convert = each.lower()
    palindrome += convert[::-1]

if (string == palindrome):
    print(True)
else:
    print(False)
