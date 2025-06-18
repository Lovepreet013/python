from collections import OrderedDict #for ordered dictionaries

#dictionary keys can be string or number

#unordered dictionaries
ages = { 
    "peter" : 21,
    "john" : 22,
}

# print(ages["peter"])

# for key, value in ages.items():
#     print(f"{key} is {value} years old.")

address = dict()

address["peter"] = "123 Main St"
address["john"] = "456 Elm St"

# for key, value in address.items():
#     print(f'{key} lives at {value}.')

#ordered dictionaries : maintain the order of insertion

ordered_dictionary = OrderedDict()

ordered_dictionary["peter"] = 21
ordered_dictionary["john"] = 22
ordered_dictionary["mary"] = 23

students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}

# print(students)
# print(students['Peter'])
# print(students['Peter']['address'])

for key, value in students.items():
    print("\nPerson : ", key)
    for key_value in value:
        print(key_value + ':', value[key_value])