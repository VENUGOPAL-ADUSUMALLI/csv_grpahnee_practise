# pass by value is in the python is immutable objects like int,string,tuple.
# pass by reference is in the python is mutable objects like list,set
#
print("----------------- matrix rotation clock wise----------------------")
rows = int(input("Enter no:of rows: "))
columns = int(input("Enter no:of Columns :"))
matrix = []
print("Enter matrix values")
for i in range(rows):
    matrix_input = list(map(int, input().split()))
    matrix.append(matrix_input)
final_matrix = matrix[::-1]
# resultant_matrix = list(zip(*final_matrix))
# print(resultant_matrix)
finaL_rotation_matrix = []
length_of_matrix = len(matrix) - 1
for i in range(rows):
    temp_list = []
    for j in range(columns):
        temp_list.append(matrix[length_of_matrix - j][i])
    finaL_rotation_matrix.append(temp_list)
print(finaL_rotation_matrix)

# print("--------------------------------fibonacci---------------------")
#
#
# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# result_fibonacci = fibonacci(5)
# print(result_fibonacci)

# # ----------------------db models--------------------------
# # discussion  user_id    comments:                         reactions:    comment reaction:
# #    user(FK)            discussion_id(FK)                 id             comment_id(FK)
# #                          user_id(FK)                                    reaction_id(FK)
# #                          parent_Comment(self relation)                  user_id(FK)
#
#
# # abstraction Practise
# from abc import ABC, abstractmethod
#
#
# class paymentGateway(ABC):
#     @abstractmethod
#     def authentication(self):
#         pass
#
#     @abstractmethod
#     def pay(self, amount):
#         pass
#
#
# class RazorpayImplementation(paymentGateway):
#     def authentication(self):
#         print("This user have access")
#
#     def pay(self, amount):
#         print(f"{amount} paid using Razorpay")
#
#
# class StripeImplementation(paymentGateway):
#     def authentication(self):
#         print("This user have access")
#
#     def pay(self, amount):
#         print(f"{amount} paid using stripe")
#
#
# def completePayment(gateway: paymentGateway, amount):
#     gateway.authentication()
#     gateway.pay(amount)
#
#
# completePayment(RazorpayImplementation(), 500)
# completePayment(StripeImplementation(), 1000)


# --------------------------------> adapter------------------------>


# class JsonDataProvider:
#     def get_json(self):
#         return {
#             "name": "Venu",
#             "role": "Backend Developer"
#         }
#
#
# class DataClientInterface:
#     def get_data(self):
#         """Return data in XML format"""
#         pass
#
#
# class JsonToXmlConvertAdapter(DataClientInterface):
#     def __init__(self, data_provider):
#         self.data_provider = data_provider
#
#     def get_data(self):
#         json_data = self.data_provider.get_json()
#         xml_data = "<data>\n"
#         for key, value in json_data.items():
#             xml_data += f"  <{key}>{value}</{key}>\n"
#         xml_data += "</data>"
#         return xml_data
#
#
# adapter = JsonToXmlConvertAdapter(JsonDataProvider())
# print(adapter.get_data())
# ------------------------------>DB indexes------------------------>
