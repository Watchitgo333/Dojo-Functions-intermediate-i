# 1. Update Values in Dictionaries and Lists
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# x[1] [0] = 15
# students[0] ['last_name'] = 'Bryant'
# sports_directory['soccer'] [0] = 'Andres'
# z[0] ['y'] = 30
# print(x)
# print(students)
# print(sports_directory)
# print(z)

# 2. Iterate Through a List of Dictionaries
# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary(students):
#     count = 0
#     name = ''
#     comma = ","
#     for x in range(0, len(students)):
#         for key, val in students[x].items():
#             name += f"{key} - {val}{comma} "
#             count += 1
#             comma = ""
#             if count == 2:
#                 print(name)
#                 count = 0
#                 name = ''
#                 comma = ","

# iterateDictionary(students)

# 3. Get Values From a List of Dictionaries

# def iterateDictionary2(keys, list):
#     for x in range(0, len(list)):
#             print(students[x][keys])

# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

# 4. Iterate Through a Dictionary with List Values
# print("---------------")
# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# def printInfo(dict):
#     for key, val in dict.items():
#         print(len(val), key.upper())
#         for x in range(0, len(val)):
#             print(val[x])
#             if x == len(val)-1:
#                 print("--------------------")

# printInfo(dojo)
