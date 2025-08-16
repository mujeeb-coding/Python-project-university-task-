import json

# Sample student records
students = [
    {"id": 1, "name": "Ali", "grade": "A"},
    {"id": 2, "name": "Sara", "grade": "B"},
    {"id": 3, "name": "Ahmed", "grade": "A+"}
]

# Save to JSON
with open('students.json', 'w') as f:
    json.dump(students, f, indent=4)

# Read and print from JSON
with open('students.json') as f:
    loaded_students = json.load(f)

print("Loaded Students:")
for student in loaded_students:
    print(student)
