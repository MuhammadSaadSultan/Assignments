# Nested Dictionaries:

# Create a nested dictionary to represent the following data:

#  Person:  
#   Name: John  
#   Age: 30  
#   Address:  
#     Street: 123 Elm St  
#     City: Boston


person = {
    "Name": "John",
    "Age": 30,
    "Address": {
        "Street": "123 Elm St",
        "City": "Boston"
    }
}

print("Person's Name:", person["Name"])
print("Person's Age:", person["Age"])
print("Street:", person["Address"]["Street"])
print("City:", person["Address"]["City"])
