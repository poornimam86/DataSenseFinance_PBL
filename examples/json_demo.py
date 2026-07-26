import json

student = {
    "id": 101,
    "name": "Ravi",
    "marks": 95
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON File Created Successfully!")