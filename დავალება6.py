my_dict = {
  "students": [
    {"id": 20, "name": "Giorgi", "age": 25},
    {"id": 25, "name": "Giorgi", "age": 23},
    {"id": 56, "name": "Nika", "age": 25},
    {"id": 100, "name": "Nika", "age": 22},
    {"id": 1232, "name": "Dato", "age": 22},
    {"id": 846723, "name": "Archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "56": "B", "100": "A", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "56": "B", "100": "A", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "56": "A", "100": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
  ]
}

print("Student IDs - 20, 25, 56, 100, 1232, 846723")
stud_id = int(input("Enter An ID: "))

for student in my_dict["students"]:

   while stud_id == student["id"]:

    st_id = student["id"]
    st_name = student["name"]
    st_age = student["age"]
    print(f"ID:{st_id}, Name:{st_name}, Age:{st_age}")

    for subject in my_dict["subjects"]:

      sub_id = subject["id"]
      sub_name = subject["name"]
      st_grades = subject["grades"][str(st_id)]

      print(f"subject: {sub_name}, grade: {st_grades}")

    break
  
     
  
      
      
      
      

      
      

