import json

with open('students.json', 'r') as f:
  data = json.load(f)

  print("Students who are 19 years old:")
  for student in[student for student in data if student['age'] == 19]:
    print(f"Student ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")
      
  print("\nStudents whose name end with 'a':")
  for student in [student for student in data if student['name'].split()[0].endswith('a')]:
    print(f"Student ID: {student['id']}, Name: {student['name']}")

  print("\nStudents who study math:")
  for student in [student for student in data if 'Math' in student['courses']]:
    print(f"Student ID: {student['id']}, Name: {student['name']}, Course: {student['courses']}")