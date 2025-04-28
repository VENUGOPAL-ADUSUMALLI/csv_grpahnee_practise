# def magical_sum(n):
#     if n == 0:
#         return n
#     return n % 10 + magical_sum(n // 10)
#
#
# result_magical_sum = magical_sum(1234)
# print(result_magical_sum)
#
#
# def reverse_spell(s):
#     if len(s) == 1:
#         return s
#     return reverse_spell(s[1:]) + s[0]
#
#
# result_reverse_spell = reverse_spell("venu")
# print(result_reverse_spell)
#
#
# def print_subsequence(index, array, path):
#     if (index == len(array)):
#         print(path)
#         return
#     print_subsequence(index + 1, array, path + [array[index]])
#     print_subsequence(index + 1, array, path)
#
#
# array = [1, 2]
# print_subsequence(0, array, [])
#
# print("---------------- subsequence------------------")
#
#
# def subsequence(index, sum_subsequence_list, path, target):
#     if index == len(sum_subsequence_list):
#         if (sum(path) == target):
#             print(path)
#         return
#     subsequence(index + 1, sum_subsequence_list, path + [sum_subsequence_list[index]], target)
#     subsequence(index + 1, sum_subsequence_list, path, target)
#
#
# sum_subsequence_list = [1, 2, 3]
# target = 3
# subsequence(0, sum_subsequence_list, [], target)
#
# print("-----------------------------------------word chain builder -------------------------------")
#
#
# def word_chain_builder(index, words_list, path, unique_list, last_letter):
#     if index == len(words_list):
#         print(path)
#         return
#     length_of_words_list = len(words_list)
#     for i in range(index + 1, length_of_words_list):
#         if words_list[i] not in unique_list and words_list[i][0] == last_letter:
#             unique_list.append(words_list[index + 1])
#             word_chain_builder(index + 1, words_list, path + [words_list[index + 1]],
#                                unique_list, words_list[index + 1][-1])
#         else:
#             word_chain_builder(index, words_list, path, unique_list, last_letter)
#
#
# words_list = ["apple", "egg", "goat", "tree"]
# last_letter = words_list[0][-1]
# word_chain_builder(0, words_list, [words_list[0]], [], last_letter)
#
#
# def subsets(nums, path, index):
#     if index == len(nums):
#         print(path)
#         return
#     subsets(nums, path + [nums[index]], index + 1)
#     subsets(nums, path, index + 1)
#     return
#
#
# nums = [1, 2, 3]
# subsets(nums, [], 0)


def reverseAnArray(new_list):
    if len(new_list) == 0:
        return new_list
    return reverseAnArray(new_list[1:]) + [new_list[0]]


new_list = [1, 2, 3, 4, 5]
result = reverseAnArray(new_list)
print(result)
