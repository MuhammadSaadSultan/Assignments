# ↪ Iterate through the dictionary student and print all key-value 
# pairs in the format key: value.


student = {
    "name": "Ahmad Ali",
    "age": 24,
    "Uni": "GC"
}

for key, value in student.items():
    print(f"{key}: {value}")
