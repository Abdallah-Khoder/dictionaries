# def merge_dictionaries(dic1,dic2): 
#     print(dic1)
#     print(dic2)
#     dic1_sort = dict(sorted(dic1.items()))
#     dic2_sort = dict(sorted(dic2.items()))
#     dic1_sort.update(dic2_sort) 
#     print(dic1_sort)
# dict1 = {"c": 6, "a": 2, "b": 3}
# dict2 = {"b": 10, "d": 4}
# merge_dictionaries(dict1 , dict2)

# sentence = input("Enter a sentence : ")
# words = sentence.split() 
# print(words)
# repeat = 0 
# dictionaries = {}
# for i in range(len(words)):
#     if words[i] not in dictionaries:
#         repeat = 0  
#         for j in range(len(words)):
#             if(words[i] == words[j]) : 
#                 repeat += 1 
#         dictionaries.update({words[i] : repeat})

# print(dictionaries)

# company_employees = {
# "Engineering": {
# "Alice": {"age": 30, "role": "Software Engineer"},
# "Bob": {"age": 28, "role": "DevOps Engineer"}
# },
# "HR": {
# "Charlie": {"age": 35, "role": "HR Manager"}
# }
# }
# branch = input("add a new employe in branch : ")
# if(branch  in company_employees) : 
#     employee_name = input("Enter employee name: ")
#     age = input("Enter employee age: ")
#     role = input("Enter employee role: ")
#     company_employees[branch][employee_name] = {"age": age, "role": role}
# else : 
#     print(f"Branch '{branch}' does not exist!")
# print(company_employees)

# def count_employee(dic): 
#     count_employe = 0 
#     for i in dic.values():
#         count_employe+= len(i)
#     return count_employe

# print(count_employee(company_employees))

dictionaries = input("enter a dictionaries : ")
dictionaries = eval(dictionaries)
new_dictionaries = {}
for key,value in dictionaries.items() : 
    if(value not in new_dictionaries) : 
        new_dictionaries[value] = []
    new_dictionaries[value].append(key)

print(new_dictionaries)