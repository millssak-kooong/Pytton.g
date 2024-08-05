# my_dict = {'name': 'Alice', 'age': 25}
# print(my_dict)

# # ---------------------------------------
# my_dict = dict(name = "Alice", age = 25, country = "USA")
# print(my_dict)

# # ---------------------------------------
# pairs = [("name", "Alice"), ("age", 25), ("country", "USA")]
# mydict = dict(pairs)
# print(my_dict)

# # ---------------------------------------
# keys = ["name", "age", "country"]
# values = ["Alice", 25, "USA"]
# my_dict = dict(zip(keys, values))
# print(my_dict)

# #########################################
# contact = {"name" : "John Doe", \
#            "email" : "john.doe.@example.com", \
#             "phone" : "123-456-7890"}

# print("Name:", contact["name"])
# print("Email:", contact["email"])
# print("Phone:", contact["phone"])

# contact["email"] = "new.email.@example.com"
# contact["phone"] = "987-654-3210"
# contact["address"] = "1234 Main St" # 새 Key를 추가
# print("\nUpdated:", contact)

# del contact["phone"]
# print("\nDeleted phone:", contact)

# # contact.clear()

#########################################
person = {'name' : 'John', 'age' : 30, 'city' : 'New York'}

for key in person:
    print(f'Key: {key}, Value: {person[key]}')